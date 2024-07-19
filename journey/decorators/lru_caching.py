from functools import lru_cache

@lru_cache(maxsize=2)
def add(x, y):
    print('Calculating...')
    return x + y

print(add(1, 2))
print(add(1, 2))
print(add(2, 3))
print(add(2, 3))
print(add(2, 3))