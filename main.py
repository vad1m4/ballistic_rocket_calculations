import math


def angleRound(x, base=15):
    return base * round(x / base)


def checkRange(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    c = math.sqrt(pow(a, 2) + pow(b, 2))
    return c


def attackAngle(c):
    global attack_range_fixed
    if c < 21500:
        if c <= 20000:
            if c <= 19000:
                if c <= 15000:
                    # if c <= 9500:
                    #     return(90)
                    # return(75)
                    return 90
                attack_range_fixed = 18500
                return 45
            attack_range_fixed = 19600
            return 15
        attack_range_fixed = 20900
        return 30
    return 90


def attackOrientationAngle(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    angle = (math.atan(a / b)) / (math.pi / 180)
    angle = angleRound(angle)
    return angle


def attackCoordinates(x1, y1, c, angle):
    a = c * math.sin(angle * (math.pi / 180))
    b = c * math.cos(angle * (math.pi / 180))
    # print(f"cos ang {math.cos(angle)}")
    # print(f"sin ang {math.sin(angle)}")
    # print(f"angle = {abs(angle)}")
    # print(f"a = {a}")
    # print(f"b = {b}")
    # if x1 > a:
    #     x = x1 - abs(a)
    # else:
    #     x = a - abs(x1)

    # if y1 > b:
    #     y = y1 - abs(b)
    # else:
    #     y = b - abs(y1)
    # return (round(x, 1), round(y, 1))

    if x1 > a:
        if x1 < 0 and a < 0:
            # print(x1 - a)
            x = x1 - a
        else:
            # print(x1 - abs(a))
            x = x1 - abs(a)
    else:
        if x1 < 0 and a < 0:
            # print(a - x1)
            x = a - x1
        else:
            # print(a - abs(x1))
            x = a - abs(x1)

    if y1 > b:
        if y1 < 0 and b < 0:
            # print(y1 - b)
            y = y1 - b
        else:
            # print(y1 - abs(b))
            y = y1 - abs(b)
    else:
        if y1 < 0 and b < 0:
            # print(b - y1)
            y = b - y1
        else:
            # print(b - abs(y1))
            y = b - abs(y1)
    return (round(x, 1), round(y, 1))


# print(a-x1)
# print(b-y1)


targ_x, targ_y = input("Input target's x and y coordinates: ").split(" ")
targ_x, targ_y = int(targ_x), int(targ_y)

sender_x, sender_y = input("Input your x and y coordinates: ").split(" ")
sender_x, sender_y = int(sender_x), int(sender_y)


attack_range = checkRange(targ_x, targ_y, sender_x, sender_y)
if attack_range != 0:
    attack_angle = attackAngle(attack_range)
    attack_orientation_angle = attackOrientationAngle(
        targ_x, targ_y, sender_x, sender_y
    )
    print(f"Target range: {round(attack_range, 1)}")
    print(f"Attack orientation angle required: {attack_orientation_angle}")
    print(f"Optimal attack angle: {attack_angle}")
    attack_x, attack_y = attackCoordinates(
        targ_x, targ_y, attack_range_fixed, attack_orientation_angle
    )
    print(f"Optimal launch coordinates are: {attack_x} {attack_y} (x, y)")
    print(f"Full list: ")
    print(f"Attack angle #1: {15.0}")
    attack_x, attack_y = attackCoordinates(
        targ_x, targ_y, 19600, attack_orientation_angle
    )
    print(f"Optimal launch coordinates are: {attack_x} {attack_y} (x, y)")
    print(f"Attack angle #2: {30.0}")
    attack_x, attack_y = attackCoordinates(
        targ_x, targ_y, 20900, attack_orientation_angle
    )
    print(f"Optimal launch coordinates are: {attack_x} {attack_y} (x, y)")
    print(f"Attack angle #3: {45.0}")
    attack_x, attack_y = attackCoordinates(
        targ_x, targ_y, 18500, attack_orientation_angle
    )
    print(f"Optimal launch coordinates are: {attack_x} {attack_y} (x, y)")


# 15300
# -15300


# math.cos()
