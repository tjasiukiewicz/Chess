#!/usr/bin/env python3

# Uwaga: Kod rzuca wyjątkiem i jest to jak najbardziej zamierzone.

from copy import copy, deepcopy

def Memento(obj, deep=False):
    state = copy(obj.__dict__) if deep else deepcopy(obj.__dict__)

    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore


class Transaction:
    """Strażnik transakcji.
    """
    deep = False
    states = []

    def __init__(self, *targets):
        self.targets = targets
        self.commit()

    def commit(self):
        self.states = [Memento(target, self.deep) for target in self.targets]

    def rollback(self):
        for a_state in self.states:
            a_state()


class Transactional(object):
    """Dekorator transakcyjny do metod. Metoda odtwarzana jest do stanu przed wykonaniem jeśli rzucony będzie
    wyjątek.
    """

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, T):
        def transaction(*args, **kwargs):
            state = Memento(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except Exception as e:
                state()
                raise e

        return transaction


class NumObj(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.value)

    def increment(self):
        self.value += 1

    @Transactional
    def operation(self):
        self.value = '1111'  # <- Nieprawidłowa wartość
        self.increment()  # <- będzie rollback


if __name__ == '__main__':
    num_obj = NumObj(-1)
    print(num_obj)

    a_transaction = Transaction(num_obj)
    try:
        for i in range(3):
            num_obj.increment()
            print(num_obj)
        a_transaction.commit()
        print('-- committed')

        for i in range(3):
            num_obj.increment()
            print(num_obj)
        num_obj.value += 'x'  # Tu ma być załamanie i wyjątek
        print(num_obj)
    except Exception as e:
        a_transaction.rollback()
        print('-- rolled back')
    print(num_obj)

    print('-- operation ...')
    try:
        num_obj.operation()
    except Exception as e:
        print('-> operation fail!')
        import sys
        import traceback

        traceback.print_exc(file=sys.stdout)
    print(num_obj)

