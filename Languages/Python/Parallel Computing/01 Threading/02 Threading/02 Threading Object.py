# python -m Parallel\ Computing/Asynchronous/02\ Threading/02\ Threading\ Object
import threading
import time
from concurrent.futures import ThreadPoolExecutor


## 1. Lock (MutEx) (Mutually Exclusive)
"""
What:
- It is synchronisation technique
- A one thread can acquire a lock at a time.
- If another thread tries to acquire it, it waits until it is released

Use Case:
- Protect Critical Section, where shared resource are modified
- Prevent race condition

Analogy:
- A bathroom with a key:
  Whoever takes the key goes inside
  Others must wait until the key is returned
"""
shared_resource = 0
lock = threading.Lock()
with lock: # Only one thread inside this block at a time
    shared_resource += 1


# 2. Rlock (Reentrant Lock) (Re-Entrant)
"""
What:
- A lock that can be acquired multiple times by the same thread without deadlocking.
- Normal Lock → if you acquire it twice from the same thread, you’ll block yourself.

Use Case:
- When functions are nested and both need to acquire the same lock.

Analogy:
- You lock your apartment door.
- You can open/close inner rooms without giving the key back each time — since it’s still you holding the master key.
"""

lock = threading.RLock()
def outer():
    with lock:
        inner()

def inner():
    with lock:
        print("Safe to enter again")

if __name__ == "__main__1":

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(outer)

# 3. Semaphore
"""
What:
- A counter-based lock that allows up to N threads to access a resource at once.
- Starts with a value (say 3) → at most 3 threads can acquire it simultaneously.

Use Case:
Limit concurrency:
   - Database connection pool
   - Thread-safe API rate limiter

Analogy:
A parking lot with 3 slots
   - At most 3 cars can park.
   - Others wait until a car leaves.
"""

semaphore = threading.Semaphore(3)

def worker(i):

    with semaphore:
        print(f"{i} is using Resource")
        time.sleep(3)

if __name__ == "__main__2":

    with ThreadPoolExecutor(max_workers=6) as executor:
        for i in range(6):
            executor.submit(worker, i+1)

# Note: Even though I have 6 workers only 3 of them runs simultaneously
# Semaphore(1) will behave as lock
# Semaphore should be used only when tasks are parallelizable. If work is to update the critical section then it will behave unexpectedly.



# 4. Condition
"""
What:
- A lock + signalling mechanism
- Threads can wait for some condition and be notified when ready.

Use Case:
Producer-Consumer Problem:
- Produce created data and notifies consumer.
- Consumer waits until data is available.

Analogy:
- A restaurant:
   Customer wants food.
   Chef prepares and signals when food is ready.
"""
condition = threading.Condition()
queue = []

def consumer():
    with condition:
        while not queue:
            condition.wait()  # Wait until notified
        item = queue.pop(0)
        print("Consumed", item)

def producer(item):
    with condition:
        queue.append(item)
        condition.notify()


# 5. Barrier
"""
What:
- Synchronisation point for multiple threads
- All threads wait at the barrier until the last one arrives, then they all proceed together.

Use Case:
- Parallel Computation in steps (Phases)
- 4 threads each compute a part of datasets, then synchronize before moving to the next steps.
- Lets say a worker has to compute 2 tasks in parallel: a) Add 1 to number and then multiply sum of results to each number
  - Each thread will add 1 to number
  - Wait until all threads are completed [Barrier: Wait until threads are complete]
  - Then compute their sum
  - Then add the sum to each number

Analogy:
- Race Start line:
  - All runners wait until everyone is ready
  - Only then race starts
"""

barrier = threading.Barrier(3)
list_ = [1, 2, 3]

def worker(list_, i):
    # Phase 1: Add 1
    print(f"Add 1 to {list_[i]}")
    list_[i] += 1
    print(f"{i + 1} is waiting at barrier")

    # Wait for all threads to finish (in this case 3 threads)
    barrier.wait()
    print(f"{i+1} Passed barrier")
    print(f"List after first barrier: {list_}")

    # Compute Sum
    sum_ = sum(list_)

    # Wait for all threads to calculate sum and then move them to update the list
    barrier.wait()

    # Multiply each with Sum
    print(f"Multiply {sum_} to {list_[i]}")
    list_[i] *= sum_

if __name__ == "__main__":

    with ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(len(list_)):
            executor.submit(worker, list_, i)

    print(f"Final List is {list_}")

# 6. Event
"""
What:
- A simple flag shared between threads.
- One thread sets the event (set()), others can wait for it (wait()).

Use Case:
- Coordination between threads.
- Example: start multiple workers only after initialization is complete.

Analogy:
A traffic light:
   Cars (threads) wait at red.
   When the signal goes green (set()), all cars move.
"""

# Difference between Event and Condition
# | Feature                | `Event`                                                                | `Condition`                                                             |
# | ---------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------- |
# | **Type**               | Boolean flag                                                           | Lock + wait/notify                                                      |
# | **Use case**           | Simple state signaling (start/stop)                                    | Complex resource coordination (queues, shared state)                    |
# | **Wait**               | `event.wait()` blocks until flag is set                                | `condition.wait()` blocks until `notify()` is called                    |
# | **Who wakes threads?** | `event.set()` (persistent until cleared)                               | `condition.notify()` or `notify_all()`                                  |
# | **State remembered?**  | Yes — once set, all future `wait()` return immediately until `clear()` | No — if no one is waiting when `notify()` is called, the signal is lost |
# | **One-to-many?**       | Natural — all waiters wake on `set()`                                  | By default `notify()` wakes 1, `notify_all()` wakes all                 |

event = threading.Event()

def worker():
    print("Waiting for event...")
    event.wait()
    print("Event triggered!")

event.set()  # Signal all waiters

# 7. Timer
"""
What:
- A thread that runs a function after a delay.

Use Case:
- Scheduled tasks, retry mechanisms.

Analogy:
- Alarm clock — goes off after a set time.
"""
timer = threading.Timer(5, lambda: print("Hello after 5s"))
timer.start()



