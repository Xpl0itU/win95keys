import functools
import random

def multiple(m):
    return True if m % 7 == 0 else False

@functools.lru_cache
def oem():
    firstPart = str(random.randint(1, 366)) + str(random.randint(95, 99))
    thirdPart = random.randint(100000, 999999)
    sumAll = thirdPart

    while not multiple(sumAll):
        thirdPart = random.randint(100000, 999999)
        sumAll = thirdPart

    lastPart = str(random.randint(10000, 99999))

    return str(firstPart) + "-OEM-" + "0" + str(thirdPart) + "-" + lastPart
