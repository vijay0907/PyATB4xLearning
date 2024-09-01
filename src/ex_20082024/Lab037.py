# Conditions and Loops

# Write a program to take a user age and let him know if he can go to the club
# age limit 21

# Logic Building
# user input --> data type --> inr
# output --> String


# Rough logic
# age > 21 --> print can go
# age < 21 --> print can't go


# Write the logic
age = input("Enter your age: ")
age = int(age)

if age >= 21:
    print(f"Your age is {age} so can go to Club")
else:
    print(f"Your age is {age} so can't go to Club")
