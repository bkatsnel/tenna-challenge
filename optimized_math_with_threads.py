import threading

# Lock Global Variable
shared_resource_lock = threading.Lock()

# Shared Global Variable
number_with_lock = 1

# Global Varaibles
COUNT = 100
THREADS = 2
TIMEOUT = 5

class myThread(threading.Thread):

    def __init__(self, threadID, events):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.events = events
        self.reminder = threadID % THREADS

    def run(self):
        global number_with_lock
        # Wait for threads to start
        self.events[self.threadID - 1].set()
        for i in range(0,len(self.events)):
            if i != self.threadID - 1:
               self.events[i].wait(TIMEOUT)
        # Increment number
        print ("Starting Tread " + str(self.threadID) + "\n")
        while True:
            shared_resource_lock.acquire()
            if (number_with_lock <= COUNT and (number_with_lock%THREADS) == self.reminder):
                print ("Thread %d: Number %d" % (self.threadID, number_with_lock))
                number_with_lock += 1
            shared_resource_lock.release()
            if number_with_lock > COUNT:
                break
        # Print end of thread messsgae
        print ("Exiting Thread " + str(self.threadID) + "\n")

#Main program
if __name__ == '__main__':

    threads = []
    events = []

    # Create Events to Sync Threads
    for i in range(THREADS):
        events.append(threading.Event())

    # Create Thereads
    for i in range(THREADS):
        threads.append(myThread(i+1, events))

    # Start the Threads created
    for i in range(THREADS):
        threads[i].start()

    # Wait for all thread to complete 
    for i in range(THREADS):
        threads[i].join()

    print ("Exiting Main Thread")