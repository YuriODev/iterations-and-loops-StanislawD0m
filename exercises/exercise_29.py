# Your solution to Exercise 29
# python -m unittest tests/test_exercise_29.py
number = int(input())
total = number
sum_of_squares = number ** 2
while total != 0:
    number = int(input())
    sum_of_squares += abs(number) ** 2
    total += number
print(sum_of_squares)
