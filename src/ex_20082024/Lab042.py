# Grade Calculator
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D or F)
# based on the following grading scale
#
# A: 90 - 100
# B: 80 - 89
# C: 70 - 79
# D: 60 - 69
# F: 0 - 59

# Logic Building Formula

# 1 User inputs --> Score --> int
# 2 Output --> Str --> Grade

score = int(input("Enter your mark :"))

# score >= 90 and score<= 100 --> "A"
# score >= 80 and score<= 89 --> "B"

if 90<= score <= 100:  # Simplified chaining format --> 90<= score <= 100
    print("Your grade is ", "A")
elif 80<= score <= 89:
    print("Your grade is ", "B")
elif 70<= score <= 79:
    print("Your grade is ", "C")
elif 60<= score <= 69:
    print("Your grade is ", "D")
elif score > 100:
    print("Invalid mark!!")
else:
    print("Your grade is ", "F")
