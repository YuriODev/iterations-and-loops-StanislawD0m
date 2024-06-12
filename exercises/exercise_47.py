# Your solution to Exercise 47
# python -m unittest tests/test_exercise_47.py
n = int(input("Enter an integer: "))
for i in range(1, n + 1):
    reversed_integer = 0
    original_integer = i
    while original_integer != 0:
        digit = original_integer % 10
        reversed_integer = reversed_integer * 10 + digit
        original_integer //= 10
    if i == reversed_integer:
        print(i, end=" ")