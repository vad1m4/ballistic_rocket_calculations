import math as m


def angle_round(x, base=15):
    return base * round(x / base)


# def check_range(x_1, y_1, x_2, y_2):

#     # a = x_2 - x_1
#     # b = y_2 - y_1
#     # c = m.sqrt(pow(a, 2) + pow(b, 2))
#     return c


def attack_angle(distance):
    if distance < 17000 or distance > 21400:
        return 0, distance
    else:
        if distance <= 21400 and distance > 20400:
            return 30, 20900
        if distance <= 20400 and distance > 19000:
            return 15, 20200
        if distance <= 19000 and distance >= 17000:
            return 45, 18500


def orientation_angle(x_1, y_1, x_2, y_2):
    a = x_2 - x_1
    b = y_2 - y_1
    angle = m.degrees(m.atan2(a, b))
    angle = angle_round(angle)
    return m.radians(angle)

def orientation_angle_1(x_1, y_1, x_2, y_2):
    a = x_2 - x_1
    b = y_2 - y_1
    angle = m.degrees(m.atan2(b, a))
    angle = angle_round(angle)
    return m.radians(angle)


def attack_coords(target_x, target_y, angle, distance):
    # need to get to 11292 -8516
    # -10503 18068
    # 809, 9517
    # print(m.sin(angle))
    # print(distance)
    launch_x = m.sin(angle) * distance + target_x
    launch_y = m.cos(angle) * distance + target_y

    return round(launch_x), round(launch_y)


def main():
    sender_x, sender_y = input("Input your x and y coordinates: ").split(" ")
    sender_x, sender_y = int(sender_x), int(sender_y)

    target_x, target_y = input("Input target's x and y coordinates: ").split(" ")
    target_x, target_y = int(target_x), int(target_y)

    real_distance = round(m.dist([target_x, target_y], [sender_x, sender_y]))

    angle, distance = attack_angle(real_distance)
    print(f"Distance: {real_distance}")
    print(
        f"Optimal coordinates: {attack_coords(target_x,target_y,orientation_angle(target_x, target_y, sender_x, sender_y),distance,)}"
    )
    print(
        f"Orientation angle: {round(m.degrees(orientation_angle_1(sender_x, sender_y, target_x, target_y)))}"
    )
    print(f"Angle of attack: {angle}")


if __name__ == "__main__":
    main()
