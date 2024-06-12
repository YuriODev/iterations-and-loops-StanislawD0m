# Your solution to Exercise 21
#python -m unittest tests/test_exercise_21.py
number = int(input())
sum_of_factorials = 0
for i in range(1, number + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    sum_of_factorials += factorial
print(sum_of_factorials)