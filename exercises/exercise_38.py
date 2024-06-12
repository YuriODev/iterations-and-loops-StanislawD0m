# Your solution to Exercise 38
# python -m unittest tests/test_exercise_38.py
n = int(input("Enter a number: "))
max_digit = 0
min_digit = 9
while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
    n //= 10
even_difference = (max_digit - min_digit) % 2 == 0
print(even_difference)