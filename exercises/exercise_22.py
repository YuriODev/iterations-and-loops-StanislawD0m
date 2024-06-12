# Your solution to Exercise 22
# python -m unittest tests/test_exercise_22.py
num = int(input())
while num > 0:
    print(num)
    num //= 10
else:
    print(num)