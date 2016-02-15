import math

x = int(input())
y = int(input())


def division(x, y):
    if not x or not y:
        return None

    if y == 0:
        return None

    if x == 0:
        return 0

    is_negative = False

    if x < 0 or y < 0:
        if x < 0:
            x = -x
            is_negative = True
        if y < 0:
            y = -y
            if is_negative:
                is_negative = False
            else:
                is_negative = True

    if x < 0 and y < 0:
        x = -x
        y = -y
        is_negative = False

    tmp = x
    quotient = 0
    while abs(tmp) >= y:
        tmp -= y
        quotient += 1

    if is_negative:
        return -quotient
    else:
        return quotient


ans = division(x, y)
if ans is not None:
    print(ans)
else:
    print("Wrong input")
