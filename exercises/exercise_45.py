# Your solution to Exercise 45
# python -m unittest tests/test_exercise_45.py
n = int(input("Enter a number: "))
sign_changes = 0
sign = 1 if n > 0 else -1
while n != 0:
    n = int(input(""))
    if sign * n < 0:
        sign_changes += 1
        sign = -sign
print(sign_changes)