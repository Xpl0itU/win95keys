import random

def multiple(m):
    return True if m % 7 == 0 else False

def oem():
    firstPart = str(random.randint(1, 366)) + str(random.randint(95, 99))

    thirdPart = "0" + str(random.randint(100000, 999999))
    sumAll = 0

    for num in thirdPart:
        sumAll += int(num)

    while not multiple(sumAll):
        thirdPart = "0" + str(random.randint(100000, 999999))
        sumAll = 0

        for num in thirdPart:
            sumAll += int(num)

    lastPart = str(random.randint(10000, 99999))

    return firstPart + "-OEM-" + thirdPart + "-" + lastPart