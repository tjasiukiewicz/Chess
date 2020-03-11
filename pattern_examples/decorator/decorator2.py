#!/usr/bin/env python3.4

def signed_return(function):
    """ Dekorator funkcji sprawdzający czy wynik jest dodatni"""
    def wrapper(*args, **kwargs):
        """ Wewnętrzna funkcja dekoratora"""
        answer = function(*args, **kwargs)
        assert answer >= 0, "Hey, wynik powinien być dodatni!"
        return answer
    return wrapper

# Do wywołania takiego "konstruktu", użyjemy składni dekoratora.

def calculate(a, b):
    """ Funkcja zwracająca sumę 2 argumentów"""
    return a + b

# Wywołamy funkcję z dekoratorem
print(calculate(2, 2))
#print(calculate(-2, 1))

# Sprawdzamy co wie o sobie funkcja calculate i .... niespodzianka... 
print(calculate.__doc__)
print(calculate.__name__)
# Output:
#4
# Wewnętrzna funkcja dekoratora
# wrapper
