import functools
import random

def multiple(m):
    return True if m % 7 == 0 else False

@functools.lru_cache
def cd():
    invalidNums = [333, 444, 555, 666, 777, 888]

    firstPart = random.randint(100, 998)
    for i in invalidNums:
        if firstPart == i:
            firstPart = random.randint(100, 998)

    lastPart = random.randint(1000000, 9999999)
    sumAll = lastPart

    while not multiple(sumAll):
        lastPart = random.randint(1000000, 9999999)
        sumAll = lastPart

    return str(firstPart) + "-" + str(lastPart)
