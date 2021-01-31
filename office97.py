import random

def multiple(m):
    return True if m % 7 == 0 else False

def office97():
    firstPart = random.randint(100, 999)
    firstPartlist = [int(d) for d in str(firstPart)]
    firstPartlist.append(firstPartlist[2] + 1)
    firstPart = ''.join(str(num) for num in firstPartlist)

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