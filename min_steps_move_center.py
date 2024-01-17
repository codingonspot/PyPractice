import math


def min_steps_to_move_circle_center(x, y, r, x1, y1):
    dist = math.sqrt((x - x1)**2 + (y - y1)**2)
    steps = math.ceil(dist/2*r)
    return steps


x = 3
y = 4
r = 5
x1 = 7
y1 = 9

min_steps = min_steps_to_move_circle_center(x, y, r, x1, y1)
print(f"The minimum number of steps required to move the center of the circle is: {min_steps}")
