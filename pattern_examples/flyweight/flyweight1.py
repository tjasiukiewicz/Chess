#!/usr/bin/env python3

import weakref

class FlyweightMeta(type):
    def __new__(cls, name, parents, dct):
        # pula instancji
        dct['pool'] = weakref.WeakValueDictionary()
        return super(FlyweightMeta, cls).__new__(cls, name, parents, dct)

    @staticmethod
    def _serialize_params(cls, *args, **kwargs):
        """Serializacja parametrów wejściowych do klucza.
        """
        args_list = map(str, args)
        args_list.extend([str(kwargs), cls.__name__])
        key = ''.join(args_list)
        return key

    def __call__(cls, *args, **kwargs):
        key = FlyweightMeta._serialize_params(cls, *args, **kwargs)
        pool = getattr(cls, 'pool', {})

        instance = pool.get(key)
        if not instance:
            instance = super(FlyweightMeta, cls).__call__(*args, **kwargs)
            pool[key] = instance
        return instance


class Card(object):

    """Pula obiektów z wbudowanym zliczaniem referencji."""
    _CardPool = weakref.WeakValueDictionary()

    """Implementacja Flyweight. Jeśli obiekt istnieje w puli, jest zwracany.
    Jeśli go nie ma jest kreowany.
    """
    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value + suit)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    # def __init__(self, value, suit):
    #     self.value, self.suit = value, suit

    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)


class Card2(object):
    __metaclass__ = FlyweightMeta

    def __init__(self, *args, **kwargs):
        # print('Init {}: {}'.format(self.__class__, (args, kwargs)))
        pass


if __name__ == '__main__':
    # Powyżej zakomentuj __new__ i odokomentuj __init__ aby zobaczyć różnicę
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(c1, c2)
    print(c1 == c2, c1 is c2)
    print(id(c1), id(c2))

    c1.temp = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))
    c1 = c2 = c3 = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))

    # Test z metaklasą
    cm1 = Card2('10', 'h', a=1)
    cm2 = Card2('10', 'h', a=1)
    cm3 = Card2('10', 'h', a=2)

    assert (cm1 == cm2) != cm3
    assert (cm1 is cm2) is not cm3

    del cm1

    del cm2

    del cm3

