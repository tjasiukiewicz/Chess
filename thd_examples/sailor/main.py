#!/usr/bin/env python3

import threading
import time

class Sailor:
    ROAD_WIDTH = 9
    position = ROAD_WIDTH // 2

    def __init__(self):
        self._end = threading.Event()
        self._position_lock = threading.Lock()
        self._thrdToLeft = threading.Thread(target=self.worker , args=(-1,))
        self._thrdToRight = threading.Thread(target=self.worker , args=(1,))
        self._position_lock.acquire()

    def worker(self, increment):
        while not self._end.is_set():
            time.sleep(.1 + increment * 0.01)
            with self._position_lock:
                if Sailor.position == 0 or Sailor.position == Sailor.ROAD_WIDTH:
                    self._end.set()
                    break
                Sailor.position += increment

    def start(self):
        self._thrdToLeft.start()
        self._thrdToRight.start()
        self._position_lock.release()
        while not self._end.is_set():
            time.sleep(.01)
            with self._position_lock:
                self.show_road()
        self._thrdToLeft.join()
        self._thrdToRight.join()

    def show_road(self):
        print("|" + "-" * Sailor.position + "*" + "-" * (Sailor.ROAD_WIDTH  - Sailor.position) + "|")


if __name__ == '__main__':
    sailor = Sailor()
    sailor.start()

