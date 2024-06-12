# Your solution to Exercise 17
# python -m unittest tests/test_exercise_17.py
n = int(input())
m = int(input())
for i in range(n):
    print(f"{i}\t" * m)