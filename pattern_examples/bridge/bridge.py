#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod

class Room(object):

    def __init__(self, size):
        self.size = size

    def newSize(self, size):
        self.size = size

    def getSize(self):
        return self.size

class Car(object):

    def __init__(self, size):
        self.size = size
        self.grow = 0

    # XXX: Tu mamy nietypowy interfejs w porównaniu do Room...
    def addSize(self, increment):
        self.grow += increment

    def howGrowMyCar(self):
        return self.grow

    def getSize(self):
        return self.size


class Resizer(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def resizeProcent(self, resize):
        pass

    @abstractmethod
    def showInfo(self):
        pass


class AdptRoom(Resizer):

    def __init__(self, room):
        self.room = room

    def resizeProcent(self, proc):
        size = self.room.getSize()
        size = size + (size * proc / 100 )
        self.room.newSize(size)

    def showInfo(self):
        print("Room size = " + str(self.room.getSize()))


class AdptCar(Resizer):

    def __init__(self, car):
        self.car = car

    def resizeProcent(self, proc):
        size = self.car.getSize() + self.car.howGrowMyCar()
        wcp = (size * proc) / 100
        self.car.addSize(wcp)

    def showInfo(self):
        print("Car size = " + str(self.car.getSize() + self.car.howGrowMyCar()))


if __name__ == '__main__':
    c1 = Car(100)
    r1 = Room(100)
    adc1 = AdptCar(c1)
    adr1 = AdptRoom(r1)
    collect = (adc1, adr1)
    
    for o in collect:
        o.resizeProcent(15)

    for o in collect:
        o.showInfo()
