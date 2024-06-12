# Your solution to Exercise 36
# python -m unittest tests/test_exercise_36.py
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
remainder = a % b
while remainder != 0:
    a = b
    b = remainder
    remainder = a % b
print(b)