#Write a Python program to calculate
# the area of a circle given its radius using the formula
# area=3.14 x r^2 (Pie = 3.14)
import math
from xmlrpc.client import MultiCall

# Logic Building Formula

# Step 1: Figure our the inputs and output
# input --> r --> data type --> float
# pi --> 3.14 or math.pi
# power --> pow or ** --> any

# Output --> float --> area, print area

# Step 2:
# rough logic --> area = 3.14 * pow(r,2)

# Step 3:

radius = float(input("Enter the radius of the circle : \n"))
print(radius)
area = math.pi*math.pow(radius,2)
area2 = 3.14 * (radius**2)
print("Area of the circle is: ", area)
print(f"Area of the circle is: {area:.2f}")
print("Area of the circle is: ", area2)
print(f"Area of the circle is: {area2:.2f}")

# * --> Mul
# ** --> Power
# one liner code
print(3.141592653589793 * (float(input("Enter the radius\n")) ** 2))