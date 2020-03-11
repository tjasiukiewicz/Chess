#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod

class Component(object):
    @abstractmethod
    def show(self):
        pass


class Leaf(Component):

    def __init__(self, val):
        self.val = val

    def show(self):
        print("Leaf->" + str(self.val), end=' ')


class Composite(Component):

    def __init__(self):
        self.childs = []

    def addComponent(self, com):
        self.childs.append(com)

    def show(self):
        print("Composite->", end=' ')
        for o in self.childs:
            o.show()
        print("")

if __name__ == '__main__':
    container = []
    for i in range(5):
        container.append(Composite())
    container[0].addComponent(Leaf(19))
    container[1].addComponent(Composite())
    container[3].addComponent(Leaf(31))

    c1 = Composite()
    c1.addComponent(Leaf(43))
    c1.addComponent(Leaf(654))
    container[4].addComponent(c1)

    for i in range(5):
        container[i].show()

