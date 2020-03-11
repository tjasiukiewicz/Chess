#!/usr/bin/env python3.4

def signed_return(function):
    """ Dekorator funkcji sprawdzający czy wynik jest dodatni"""
    def wrapper(*args, **kwargs):
        """ Wewnętrzna funkcja dekoratora"""
        answer = function(*args, **kwargs)
        assert answer >= 0, "Hey, wynik powinien być dodatni!"
        return answer
    wrapper.__name__ = function.__name__
    wrapper.__doc__ = function.__doc__
    return wrapper

# Do wywołania takiego "konstruktu", użyjemy składni dekoratora.
@signed_return
def calculate(a, b):
    """ Funkcja zwracająca sumę 2 argumentów"""
    return a + b

# Sprawdzamy co wie o sobie funkcja calculate i .... niespodzianka... 
print(calculate.__doc__)
print(calculate.__name__)
