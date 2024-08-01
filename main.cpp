#include <iostream>
#include <cmath>
#include <tuple>

int angle_round(int x, int base = 15)
{
    return base * round(static_cast<float>(x) / base);
}

std::tuple<int, int> attack_angle(int distance)
{
    if (distance < 17000)
    {
        return {0, 18500};
    }
    if (distance > 21400)
    {
        return {0, 20900};
    }
    else
    {
        if (distance <= 21400 && distance > 20400)
        {
            return {30, 20900};
        }
        else if (distance <= 20400 && distance > 19000)
        {
            return {15, 20200};
        }
        else if (distance <= 19000 && distance >= 17000)
        {
            return {45, 18500};
        }
    }
    return {0, distance}; // default case
}

double orientation_angle(int x1, int y1, int x2, int y2)
{
    int a = x2 - x1;
    int b = y2 - y1;
    double angle = std::atan2(static_cast<double>(a), static_cast<double>(b)) * 180 / M_PI;
    angle = angle_round(static_cast<int>(angle));
    return angle * M_PI / 180.0;
}

double orientation_angle_1(int x1, int y1, int x2, int y2)
{
    int a = x2 - x1;
    int b = y2 - y1;
    double angle = std::atan2(static_cast<double>(b), static_cast<double>(a)) * 180 / M_PI;
    angle = angle_round(static_cast<int>(angle));
    return angle * M_PI / 180.0;
}

std::pair<int, int> attack_coords(int target_x, int target_y, double angle, int distance)
{
    int launch_x = static_cast<int>(std::sin(angle) * distance + target_x);
    int launch_y = static_cast<int>(std::cos(angle) * distance + target_y);
    return {launch_x, launch_y};
}

int main()
{
    int sender_x, sender_y, target_x, target_y;
    std::cout << "Input your x and y coordinates: ";
    std::cin >> sender_x >> sender_y;

    std::cout << "Input target's x and y coordinates: ";
    std::cin >> target_x >> target_y;

    int real_distance = std::round(std::hypot(target_x - sender_x, target_y - sender_y));

    auto [angle, distance] = attack_angle(real_distance);
    auto [opt_x, opt_y] = attack_coords(target_x, target_y, orientation_angle(target_x, target_y, sender_x, sender_y), distance);
    if (angle != 0)
    {
        std::cout << "Distance: " << real_distance << "\n";
        std::cout << "Optimal coordinates: (" << opt_x << ", " << opt_y << ")\n";
        std::cout << "Orientation angle: " << std::round(orientation_angle_1(sender_x, sender_y, target_x, target_y) * 180 / M_PI) << "\n";
        std::cout << "Angle of attack: " << angle << "\n";
    }
    else
    {
        if (distance == 20900)
        {
            std::cout << "You're too far away! Closest optimal position is at (" << opt_x << ", " << opt_y << ")\n";
        }
        else
        {
            std::cout << "You're too close! Closest optimal position is at (" << opt_x << ", " << opt_y << ")\n";
        }
    }

    system("PAUSE");
    return 0;
}