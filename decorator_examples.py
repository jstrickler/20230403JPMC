import logging
from functools import wraps
from datetime import datetime

logging.basicConfig(
    filename="monitor.log",
    level = logging.DEBUG,
)

class LogFunctionCall:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        result = self._func(*args, **kwargs)
        logging.debug("calling function %s at %s with result %s",
                      self._func.__name__, datetime.now().ctime(), result)
        return result

# decorator
def log_function_call(func):

    @wraps(func)
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.debug("calling function %s at %s with result %s",
                      func.__name__, datetime.now().ctime(), result)
        return result

    return new_function   # return new function object, not its value    


def double(x):
    return x * 2

double = log_function_call(double)

@log_function_call
def triple(x):
    return x * 3

# triple = doit(triple)

print(f"double('mint'): {double('mint')}")
print(f"double.__name__: {double.__name__}")

result = triple('play')

@log_function_call
def mult(x, y):
    return x * y

print(f"mult(10, 22): {mult(10, 22)}")
print(f"mult('python is great! ', 3): {mult('python is great! ', 3)}")

print(triple.__name__, double.__name__, mult.__name__)


def spam():
    print("HEllo from spam")

spamlog = log_function_call(spam)


def animal(p1, p2):
    def deco(func):
        def replacement(*args, **kwargs):
            print(f"Params are {p1} {p2}")
            result = func(*args, **kwargs)
            return result
        return replacement
    return deco

@animal('a', 5)
def wombat():
    print("I'm a wombat")

# wombat = animal('a', 5)(wombat)
wombat()

@animal("badger", 1000)
def honeybee():
    print("I'm a honeybee")
honeybee()


@LogFunctionCall
def glork():
    print("I am a glork")


glork()


