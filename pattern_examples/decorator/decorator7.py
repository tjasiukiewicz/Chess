#!/usr/bin/env python3.4
import functools
import logging
import os

def log_call(function):
    logger = logging.getLogger("Logger")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(os.path.join("/tmp/", "log_call.log"))
    logger.addHandler(handler)
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        msg = "call: " + function.__name__ + "("
        msg += ", ".join(["{0!r}".format(a) for a in args]
            + ["{0!s} = {1!r}".format(k, v) for k, v in kwargs.items()]) + ")"
        answer = exception = None
        try:
            answer = function(*args, **kwargs)
            return answer
        except Exception as err:
            exception = err
        finally:
            msg += ("-> " + str(answer) if exception is None
                    else " raise -> {0}: {1}".format(type(exception), exception))
        logger.debug(msg)
        if exception is not None:
            raise exception
    return wrapper

@log_call
def calculate(a, b, c, data = 23):
    raise RuntimeError("Example error")
    return a

print(calculate(1, 2, 3, data = 123))
