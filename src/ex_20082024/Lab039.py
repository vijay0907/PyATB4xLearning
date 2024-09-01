# Problem to find the max between two numbers

#Logic Building Formula

# 1. User inputs --> Two float
# 2. Output --> int 1 which is max number
# 3. Input mehtod --> To get number

num1 = float(input("Enter the number1:"))
num2 = float(input("Enter the number2:"))

if num1 > num2:
    print(f"Max is {num1}")
else:
    print(f"Max is {num2}")
