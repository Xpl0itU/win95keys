import random

def multiple(m):
    return True if m % 7 == 0 else False

def cd():
    invalidNums = [333, 444, 555, 666, 777, 888, 999]

    firstPart = str(random.randint(100, 999))
    if firstPart in invalidNums:
        firstPart = str(random.randint(0, 999))

    lastPart = str(random.randint(1000000, 9999999))
    sumAll = 0

    for num in lastPart:
        sumAll += int(num)

    while not multiple(sumAll):
        lastPart = str(random.randint(1000000, 9999999))
        sumAll = 0

        for num in lastPart:
            sumAll += int(num)

    return firstPart + "-" + lastPart