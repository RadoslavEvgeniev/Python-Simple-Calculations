import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
sideA = math.fabs(x1 - x2)
sideB = math.fabs(y1 - y2)
area = sideA * sideB
perimeter = 2 * (sideA + sideB)
print(area)
print(perimeter)
