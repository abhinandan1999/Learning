# python -m Parallel\ Computing/Asynchronous/03\ Threading

import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def thread_function(name):
    logging.info(f"Thread {name} has started")
    time.sleep(2)
    logging.info(f"Thread {name} has finished")

if __name__ == "__main__1":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info(f"Main: Before creating thread")

    """
    Daemon are the process which runs in background. 
    If any thread is Deamonic then Process won't wait for it to be compeleted.
    It will end the program.
    """
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)

    logging.info(f"Main: Before starting thread")
    x.start()

    logging.info(f"Main: Wait for thread to finish")

    # Join is a Blocking Call, it will wait for the thread (x) to compelete.
    x.join()

    logging.info(f"Main: All done")

    """
    If no x.join() then flow would be:
        14:39:17: Main: Before creating thread
        14:39:17: Main: Before starting thread
        14:39:17: Thread 1 has started
        14:39:17: Main: Wait for thread to finish
        14:39:17: Main: All done 
        14:39:19: Thread 1 has finished

    if x.join() is present:
        14:41:09: Main: Before creating thread
        14:41:09: Main: Before starting thread
        14:41:09: Thread 1 has started
        14:41:09: Main: Wait for thread to finish
        14:41:11: Thread 1 has finished
        14:41:11: Main: All done
        
    """

if __name__ == "__main__2":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

    """
    Output of the Program:

    15:32:09: Main    : create and start thread 0.
    15:32:09: Thread 0 has started
    15:32:09: Main    : create and start thread 1.
    15:32:09: Thread 1 has started
    15:32:09: Main    : create and start thread 2.
    15:32:09: Thread 2 has started
    15:32:09: Main    : before joining thread 0.
    15:32:11: Thread 0 has finished
    15:32:11: Thread 1 has finished
    15:32:11: Thread 2 has finished
    15:32:11: Main    : thread 0 done
    15:32:11: Main    : before joining thread 1.
    15:32:11: Main    : thread 1 done
    15:32:11: Main    : before joining thread 2.
    15:32:11: Main    : thread 2 done
    """

if __name__ == "__main__3":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    # It is strongly recommended that you use ThreadPoolExecutor as a context manager 
    # when you can so that you never forget to .join() the threads.
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))

    """
    15:44:30: Thread 0 has started
    15:44:30: Thread 1 has started
    15:44:30: Thread 2 has started
    15:44:32: Thread 0 has finished
    15:44:32: Thread 2 has finished
    15:44:32: Thread 1 has finished
    
    """


# xxxxxxxxxxxxxxxxxx SIMULATE A RACE CONDITION xxxxxxxxxxxxxxxxxxxxx
class FakeDatabase:

    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    # Simulate reading from Database -> Process -> Update back to Database
    def update(self, name):
        logging.info("Thread %s: starting update", name)

        # Read from Database
        local_copy = self.value

        # Modify it
        local_copy += 1

        # Simulate a write operation back to database
        time.sleep(0.2)
        self.value = local_copy

        logging.info("Thread %s: finishing update", name)

    # Simulate reading from Database -> Process -> Update back to Database by preventing race condition
    def locked_update(self, name):

        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s: about to lock", name)

        with self._lock:
            logging.debug("Thread %s has lock", name)    
            # Read from Database
            local_copy = self.value

            # Modify it
            local_copy += 1

            # Simulate a write operation back to database
            time.sleep(0.2)
            self.value = local_copy

            logging.debug("Thread %s about to release lock", name)
        
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)



if __name__ == "__main__4":

    format = "%(asctime)s: %(levelname)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG,
                        datefmt="%H:%M:%S")

    # Create a instance of Database
    database = FakeDatabase() # Stores in memory of main thread
    logging.info("Testing update. Starting value is %d.", database.value)

    # Create two threads which update (Unexpected output due to race condition)
    # with ThreadPoolExecutor(max_workers=2) as executor:
    #     for i in range(2):
    #         executor.submit(database.update, i)

    # Main Thread: Variable: database
    # Thread 1: Reads the value 0, update it to 1 and before it saves the value
    # Thread 2: Reads the value 0, update it to 1 and then
    # Both Threads, update the value to 1

    # Note: Variables local to the function are always thread safe.
    # Be careful with the global variables
    

    with ThreadPoolExecutor(max_workers=2) as executor:
        for i in range(2):
            executor.submit(database.locked_update, i)
    
    logging.info("Testing update. Ending value is %d.", database.value)

    # Main Thread: Variable: database
    # Thread 1: Locks: Reads the value 0, update it to 1 and before it saves the value -> Release Lock
    # Thread 2: Locks: Reads the value 1, update it to 1 and then -> Release Lock
    # At end Database value is 2

    
# Difference between Executor.map and Executor.submit

# | Feature                     | `executor.map`                                | `executor.submit` |
# |-----------------------------|-----------------------------------------------|-------------------|
# | Submission style            | Batch-style (one function, many inputs)       | Individual tasks (any function/args) |
# | Return type                 | Iterator of results (ordered)                 | `Future` objects (manual handling) |
# | Exception handling          | Raised when you iterate results               | Stored in `Future`, you decide when to handle |
# | Order of results            | Same as input order                           | Not guaranteed (depends on task completion) |
# | Flexibility                 | Less flexible (single function only)          | More flexible (any callable, varying args) |



# xxxxxxxxxxxxxxxxxxxxxxx CRITICAL SECTIONS xxxxxxxxxxxxxxxxxxxx
"""
A Critical Section is a block of code where a thread access shared resources (like variables, list, files, database, sockets)
that must not be accessed by more than one thread at the same time.

If two or more threads enter the critical section at the same time then you get race condition - unpredictable and incorrect results.

In the given Example below: balance is a race condition
"""

import threading

def main():
    balance = 100
    def withdraw(amount):
        nonlocal balance
        # Simulate withdrawal many time
        print(f"Thread: Initial Balance is: {balance}")
        for _ in range(10_000):
            if amount <= balance:
                balance -= amount

    print(f"Initial Balance is: {balance}")

    # Create Threads
    threads = []
    for _ in range(2):
        t = threading.Thread(target=withdraw, args=(10,))
        threads.append(t)
        t.start()

    # Wait for thread to finish
    for t in threads:
        t.join()

    # Display Final Balance
    print(f"Final Balance is: {balance}")

if __name__ == "__main__":
    main()


# xxxxxxxxxxxxxxxxxxxxxxx DEADLOCKS xxxxxxxxxxxxxxxxxxxx
"""
A deadlock in programming happens when two or more threads (or processes) are waiting indefinitely
for resources that other threads are holding, and none of them can proceed.

Example:
Imaging you have two threads and two locks:
* Thread 1: Acquires Lock A and then try to Acquire Lock B
* Thread 2: Acquires Lock B and then try to Acquire Lock A

Both are now waiting on each other:


Conditions for Deadlock:
1. Mutual Exclusion: Resources that can't be shared, only one thread can use them at a time.
2. Hold and Wait: A thread hold one resource while waiting for other.
3. No Preemption: A resource can't be forcibly taken away; it must be released voluntarily.
4. Circular wait: A cycle of thread exists, each waiting for a resource held by the next.

Preventing Deadlocks:
1. Lock Ordering: Always acquire in same global order across threads.
2. Timeouts: Don't wait forever; Back off and retry
3. Try-Lock: Use non blocking attempts to acquire locks
4. Deadlock detection: Monitor resource graphs and break cycles.
"""

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_1():

    with lock_a:
        print(f"Thread 1: Acuired Lock A")
        time.sleep(1)

        print(f"Thread 1: Waiting for Lock B")
        with lock_b:
            print(f"Thread 1: Acquired Lock B")

def thread_2():

    with lock_b:
        print(f"Thread 2: Acuired Lock B")
        time.sleep(1)

        print(f"Thread 2: Waiting for Lock A")
        with lock_a:
            print(f"Thread 2: Acquired Lock A")

def thread_2_ordered():

    with lock_a:
        print(f"Thread 2: Acuired Lock A")
        time.sleep(1)

        print(f"Thread 2: Waiting for Lock B")
        with lock_b:
            print(f"Thread 2: Acquired Lock B")

if __name__ == "__main__6":

    t1 = threading.Thread(target=thread_1)
    t2 = threading.Thread(target=thread_2)
    t3 = threading.Thread(target=thread_2_ordered)

    t1.start() # It will Acuire Lock A and wait for Lock B to be released by thread 2
    # t2.start() # It will Acuire Lock B and wait for Lock B to be released by thread 1
    t3.start() # Lock Order is same as thread 1

    t1.join()
    # t2.join()
    t3.join()