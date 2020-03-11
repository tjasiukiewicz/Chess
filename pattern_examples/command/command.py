#!/usr/bin/env python3.4

from abc import ABCMeta, abstractmethod

class Command(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


class CountDown(Command):

    def execute(self):
        print("9, 8, 7, 6, 5, 4, 3, 2, 1")


class OpenValve(Command):

    def execute(self):
        print("OpenValve")


class Ignition(Command):

    def execute(self):
        print("Ignition")


class NavToMoon(Command):
    def execute(self):
        print("Go to Moon!")


class Start(object):

    def __init__(self):
        self.commands = []

    def add(self, cmd):
        self.commands.append(cmd)

    def run(self):
        for i in self.commands:
            i.execute()

if __name__ == '__main__':
    s1 = Start()
    s1.add(OpenValve())
    s1.add(CountDown())
    s1.add(Ignition())
    s1.add(NavToMoon())
    s1.run()
