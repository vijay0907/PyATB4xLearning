# Problem to find the max between three numbers
from xml.dom import SyntaxErr

# Logic Building Formula
# 1. User inputs --> num1, num2, num3 -->  integers
# 2. Output --> int or string with max number

# one condition --> if else
# more than one condition -> if elif else

# Syntax
# if condition 1:
#     print("do 1")
# elif condition 2:
#     print("do 2")
# elif condition 3:
#     print("do 3")
# else:
#     print("do 4")


num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
num3 = int(input("Enter the number3:"))

# Rough logic
# num1 > num2 and num1 > num3 --> num1 is max
# num2 > num1 and num2 > num3 --> num2 is max
# num3 is max -> Both condition is false

if num1 > num2 and num1 > num3:
    print(f"Max is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Max is {num2}")
else:
    print(f"Max is {num3}")
