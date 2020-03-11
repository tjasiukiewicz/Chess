#!/usr/bin/env python3.4
"""
Python wspiera "wstrzykiwanie" funkcji do obiektu i tu zdecydowano się tego użyć zamiast
dziedziczenia..
"""

import types


class StrategyExample:

    def __init__(self, func=None):
        self.name = 'Przykład strategii 0'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name + ' z execute 1')


def execute_replacement2(self):
    print(self.name + ' z execute 2')


if __name__ == '__main__':
    strat0 = StrategyExample()

    strat1 = StrategyExample(execute_replacement1)
    strat1.name = 'Przykład strategii 1'

    strat2 = StrategyExample(execute_replacement2)
    strat2.name = 'Przykład strategii 2'

    strat0.execute()
    strat1.execute()
    strat2.execute()
