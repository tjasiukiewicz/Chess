#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

class MyThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.name = name
        self.stop = threading.Event()
        self.sleep_period = 1.0

    def run(self):
        print("Start " + self.getName())
        count = 0
        while not self.stop.isSet():
            count += 1
            print("loop %d" % count)
            self.stop.wait(self.sleep_period)
        print("% s is finished" % self.getName())

    def join(self, timeout = None):
        self.stop.set()
        threading.Thread.join(self, timeout)

if __name__ == '__main__':
    thread1= MyThread(1, "Thr1", )
    thread2= MyThread(1, "Thr2", )
    thread1.start()
    thread2.start()
    import time
    time.sleep(4)
    thread1.join()
    thread2.join()
