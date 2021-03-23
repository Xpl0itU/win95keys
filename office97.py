import functools
import random

def multiple(m):
    return True if m % 7 == 0 else False

@functools.lru_cache
def office97():
    firstPart = random.randint(100, 999)
    firstPartlist = [int(d) for d in str(firstPart)]
    firstPartlist.append(firstPartlist[2] + 1)
    firstPart = ''.join(str(num) for num in firstPartlist)

    lastPart = random.randint(1000000, 9999999)
    sumAll = 0
    sumAll = lastPart

    if not multiple(sumAll):
        lastPart = random.randint(1000000, 9999999)
        sumAll = 0
        sumAll = lastPart

    return firstPart + "-" + str(lastPart)

