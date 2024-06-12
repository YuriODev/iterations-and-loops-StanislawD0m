# Your solution to Exercise 49
# python -m unittest tests/test_exercise_49.py
a = int(input("Enter the first four-digit number: "))
b = int(input("Enter the second four-digit number: "))
for i in range(a, b + 1):
    reversed_integer = 0
    original_integer = i
    while original_integer != 0:
        digit = original_integer % 10
        reversed_integer = reversed_integer * 10 + digit
        original_integer //= 10
    if i == reversed_integer:
        print(i, end=" ")
