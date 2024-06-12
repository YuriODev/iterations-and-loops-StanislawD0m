# Your solution to Exercise 39
# python -m unittest tests/test_exercise_39.py
n = abs(int(input()))
sum_of_digits = 0
while n != 0:
    digit = n % 10
    sum_of_digits += digit
    n //= 10
print(sum_of_digits)