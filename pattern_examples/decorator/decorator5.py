import functools

def check_call_bonduary(minimum, maximum):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            answer = function(*args, **kwargs)
            if answer > maximum:
                return maximum
            elif answer < minimum:
                return minimum
            return answer
        return wrapper
    return decorator

@check_call_bonduary(10,20)
def calculate(a):
    return a

print(calculate(19))
print(calculate(232))
print(calculate(4))
