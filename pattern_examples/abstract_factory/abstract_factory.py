#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod

class Bicycle(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def ride(self, key):
        pass

class RacingBicycle(Bicycle):
    
    def __init__(self, data):
        self.data = data

    def show(self):
        print("Racing Bike:", self.data)

    def ride(self, key):
        if key == 10:
            print("Riding Racing Bike:", self.data)
        else:
            print("***Crash Racing Bike:", self.data)

class TrackBike(Bicycle):

    def __init__(self, data):
        self.data = data

    def show(self):
        print("Track Bike:", self.data)

    def ride(self, key):
        if key == 14:
            print("Riding Track Bike:", self.data)
        else:
            print("***Crash Track Bike:", self.data)


class MountainBike(Bicycle):

    def __init__(self, data):
        self.data = data

    def show(self):
        print("Mountain Bike:", self.data)

    def ride(self, key):
        if key == 14:
            print("Riding Mountain Bike:", self.data)
        else:
            print("***Crash Mountain Bike:", self.data)


class Factory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def createTrackBicycle(self):
        pass

    @abstractmethod
    def createRecumbentBicycle(self):
        pass

    @abstractmethod
    def createEconomicBicycle(self):
        pass

    @abstractmethod
    def createRacingBicycle(self):
        pass

    @abstractmethod
    def createMountainBike(self):
        pass


class CarbonFactory(Factory):

    def createTrackBicycle(self):
        return TrackBike("Carbon normal bicycle")

    def createRecumbentBicycle(self):
        return TrackBike("Carbon recumbent bicycle")

    def createEconomicBicycle(self):
        return TrackBike("Carbon low price bicycle") # Yeah... it's possible?! :-)

    def createRacingBicycle(self):
        return RacingBicycle("Carbon racing bicycle")

    def createMountainBike(self):
        return MountainBike("Carbon mountain bike")

class AluFactory(Factory):

    def createTrackBicycle(self):
        return TrackBike("Alu normal bicycle")

    def createRecumbentBicycle(self):
        return TrackBike("Alu recumbent bicycle")

    def createEconomicBicycle(self):
        return TrackBike("Alu low price bicycle") 

    def createRacingBicycle(self):
        return RacingBicycle("Alu racing bicycle")

    def createMountainBike(self):
        return MountainBike("Alu mountain bike")


if __name__ == '__main__':
    bikeFactory1 = CarbonFactory()
    bikeFactory2 = AluFactory()
    bike1 = bikeFactory1.createTrackBicycle()
    bike2 = bikeFactory2.createRecumbentBicycle()
    bike1.show()
    bike1.ride(14)
    bike2.show()
    bike2.ride(14)
