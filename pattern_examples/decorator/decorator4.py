import functools

def signed_return(function):
    """ Dekotator funkcji sprawdzający czy wynik jest dodatni"""
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        """ Wewnętrzna funkcja dekoratora"""
        answer = function(*args, **kwargs)
        assert answer >= 0, "Hey, wynik powinien być dodatni!"
        return answer
    return wrapper

# Do wywołania takiego "konstruktu", użyjemy składni dekoratora.
@signed_return
def calculate(a, b):
    """ Funkcja zwracająca sumę 2 argumentów"""
    return a + b

# Sprawdzamy co wie o sobie funkcja calculate i .... niespodzianka... 
print(calculate.__doc__)
print(calculate.__name__)
