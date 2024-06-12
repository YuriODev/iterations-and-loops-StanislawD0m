# Your solution to Exercise 18
#python -m unittest tests/test_exercise_18.py
n = int(input())
total = 0
for i in range(n) :
    errors = int(input())
    total += errors
print(total)