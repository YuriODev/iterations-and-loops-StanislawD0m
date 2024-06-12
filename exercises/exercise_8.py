# Your solution to Exercise 8
# python -m unittest tests/test_exercise_8.py
n = int(input())
for i in range(2,n + 1,2):
    if i == n - 1 or i == n :
        print(i)
    else:
        print(i, end = " ")
        continue