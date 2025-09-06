# python Parallel\ Computing/Asynchronous/04\ Producer-Consumer.py 

import random
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import queue

SENTINEL = object()

def producer(pipeline):
    """Pretend we're getting a message from the network."""

    for message in range(2):
        # message = random.randint(1, 101)
        logging.info(f"Producer got message: {message}")
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipeline):
    """Pretend we're saving a number in the database."""

    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)



class Pipeline:
    """
    Class to allow a single element pipeline between producer and consumer.
    """
    def __init__(self):
        self.message = "a"
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire() # The moment instance of this class is create, Lock the Consumer to allow for single thread

    def get_message(self, name):
        logging.debug("%s:about to acquire getlock", name)
        self.consumer_lock.acquire()
        logging.debug("%s:have getlock", name)
        message = self.message
        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release()
        logging.debug("%s:setlock released", name)
        return message
    
    def set_message(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.debug("%s:have setlock", name)
        # logging.info(f"Setting the message: {message}")
        self.message = message
        logging.debug("%s:about to release getlock", name)
        self.consumer_lock.release()
        logging.debug("%s:getlock released", name)

def producer_queue(pipeline, event):

    while not event.is_set():
        data = random.randint(1, 100)
        logging.info("Producer got message: %s", data)
        pipeline.put(data)

    logging.info("Producer received event. Exiting")

def consumer_queue(pipeline, event):
    
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get()
        logging.info(
            "Consumer storing message: %s (size=%d)", message, pipeline.qsize()
        )

    logging.info("Consumer received event. Exiting")





if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)
    
    # Traditional way to create Producer and Consumer pipeline
    # pipeline = Pipeline()
    # with ThreadPoolExecutor(max_workers=2) as executor:
    #     executor.submit(producer, pipeline)
    #     executor.submit(consumer, pipeline)

    # logging.info(f"Final Value of Pipeline Message is: {pipeline.message}")

    # Replicate Produce and Consumer using queue
    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer_queue, pipeline, event)
        executor.submit(consumer_queue, pipeline, event)

        time.sleep(5)
        logging.info(f"Main: About to set event")
        event.set()

