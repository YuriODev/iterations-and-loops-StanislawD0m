# Your solution to Exercise 35
# python -m unittest tests/test_exercise_35.py
n = int(input("Enter an integer: "))
max_digits = 10 ** n
for i in range(max_digits - 1, 10 ** (n - 1) - 1, -2):
    print(i, end=" ")
print()