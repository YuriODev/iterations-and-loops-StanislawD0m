# Your solution to Exercise 27
# python -m unittest tests/test_exercise_27.py
n = int(input())
sum_of_series = 0
sign = 1
for i in range(1, n + 1, 2):
    sum_of_series += sign * 4 / i
    sign *= -1
print(sum_of_series)