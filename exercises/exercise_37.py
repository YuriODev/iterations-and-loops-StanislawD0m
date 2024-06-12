# Your solution to Exercise 37
# python -m unittest tests/test_exercise_37.py
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
division = 0
remainder = 0
while a >= b:
    a -= b
    division += 1
remainder = a
print(division, remainder)