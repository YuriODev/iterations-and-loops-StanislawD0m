# Your solution to Exercise 16
#python -m unittest tests/test_exercise_16.py
n = int(input())
for i in range(1,n + 1) :
    print(((n - i) * " ") + (i * "#"))