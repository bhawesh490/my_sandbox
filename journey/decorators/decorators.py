import logging
from time import perf_counter
logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.DEBUG
)
logger = logging.getLogger("Custom Logger")
logger.debug("This is a debug message")
logger.error("This is an error message")
logger.warning("This is a warning message")

def log(func):
    def inner(*args, **kargs):
        start = perf_counter()
        result = func(*args, **kargs)
        end = perf_counter() 
        logger.debug(f'called {func.__name__},elapsed = {end-start}')
        return result 
    return inner
# decorated functions
@log
def add(x, y):
    return x + y
@log
def greet(name):
    return f'Hello, {name}'  

print(add(1, 2))
print(greet('Alice'))
