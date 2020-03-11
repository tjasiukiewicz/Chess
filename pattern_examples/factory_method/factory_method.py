#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod

class Worker(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def makeReport(self):
        pass

    @abstractmethod
    def makeMedialCampaign(self):
        pass

    def getName(self):
        return self.name

class BiuroWorker(Worker):

    def __init__(self, name):
        super().__init__(name)

    def makeReport(self):
        print("1, 2, 3 Done!")

    def makeMedialCampaign(self):
        print("Eee... Eee... WTF?!?")

class MedialWorker(Worker):

    def __init__(self, name):
        super().__init__(name)

    def makeReport(self):
        print("Hey, Dude! No!")

    def makeMedialCampaign(self):
        print("1, 2, 3 Done!")

class WorkerRoom(object):

    def __init__(self):
        self.workers = []
        self.index = 0

    def newWorker(self, name, typ):
        if(typ == "Biuro"):
            self.workers.append(BiuroWorker(name))
        else:
            self.workers.append(MedialWorker(name))

    def getReport(self):
        for i in self.workers:
            print("{}:".format(i.getName()))
            i.makeReport()

    def getMedialCampaign(self):
        for i in self.workers:
            print("{}:".format(i.getName()))
            i.makeMedialCampaign()

if __name__ == '__main__':
    wr1 = WorkerRoom()
    wr1.newWorker("Adam", "Biuro")
    wr1.newWorker("Roman", "Media")
    wr1.newWorker("Fabio", "Biuro")
    wr1.newWorker("Zeb", "Media")
    print("Work Report:")
    print("-" * 20)
    wr1.getReport()
    print("Medial Campaign:")
    print("-" * 20)
    wr1.getMedialCampaign()
