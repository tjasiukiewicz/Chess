#!/usr/bin/env python3

import threading
import time

class MyThread(threading.Thread):
    counter = 2
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print("Start " + self.name)
        print_time(self.name, 5, MyThread.counter)

def print_time(threadName, delay, counter):
    while True:
        time.sleep(delay)
        print("%s %s" % (threadName, time.ctime(time.time())))
        with threadLock:
            counter -= 1
            if counter == 0:
                break

threadLock = threading.Lock()
thread1 = MyThread(1, "T1")
thread2 = MyThread(2, "T2")

thread1.start()
thread2.start()

threads = [thread1, thread2]
for t in threads:
    t.join()

print("Koniec main... ")
