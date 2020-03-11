#!/usr/bin/env python3

def calculate(a, b):
    ''' Tendencyje dodawanie
    >>> calculate(1, 1)
    2
    >>> calculate(2, 2)
    5
    >>> data = [ calculate(v, v * 2) for v in range(5) ]
    >>> data
    [0, 3, 6, 9, 12]
    >>> calculate(3, 3)
    Traceback (most recent call last):
    ...
    Exception: Durny błąd
    '''
    if a == 2 and b == 2:
        return 5
    elif a == 3 and b == 3:
        raise Exception('Durny błąd')
    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #doctest.testfile('test_data.txt')


