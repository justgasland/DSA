# code to calculate the distance between two points in a 2D space
#  y = root((x2 - x1)^2 + (y2 - y1)^2)

import math

def distance(y1, x1, y2, x2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
# Drivers Code
print("%.6f"%distance(3, 4, 4, 3))