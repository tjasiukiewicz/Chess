#!/usr/bin/env python3

from copy import deepcopy

# TODO: Powinna być abstrakcyjna... 
class Prototype(object):
    
    def clone(self):
        return self

class CompilcatedClass(Prototype):

    def __init__(self, name = "", surname = "", age = "", *args, **kwargs):
        self.name = name
        self.surname = surname
        self.age = age
        self.args = args
        self.kwargs = kwargs

    def clone(self):
        new_clone = CompilcatedClass(self.name, self.surname, self.age)
        new_clone.args = deepcopy(self.args)
        new_clone.kwargs = deepcopy(self.kwargs)
        return new_clone

    def __repr__(self):
        msg = "ComplicatedClass:\nName: {}, Surname: {}, Age: {}\nArgs: {}\nKwargs: {}".format(self.name,
                self.surname, self.age, self.args, self.kwargs)
        return msg


class Client(object):

    def go(self):
        c1 = CompilcatedClass("Adam", "Jajczarski", 67, 1, 2, 3, state = "Rencista")
        print(c1)
        c2 = c1.clone()
        c2.name = "Zenon"
        print(c2)
        print(c1)


if __name__ == '__main__':
    c1 = Client()
    c1.go()

