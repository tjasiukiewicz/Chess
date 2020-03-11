from functools import wraps, partial

def check_call_bonduary(function = None, minimum = 0, maximum = 0):
    if function is None:
        return partial(check_call_bonduary, minimum = minimum, maximum = maximum)
    @wraps(function)
    def wrapper(*args, **kwargs):
        answer = function(*args, **kwargs)
        if answer > maximum:
            return maximum
        elif answer < minimum:
            return minimum
        return answer
    return wrapper

@check_call_bonduary(minimum = 10,maximum = 20)
def calculate(a):
    return a

print(calculate(19))
print(calculate(232))
print(calculate(4))
