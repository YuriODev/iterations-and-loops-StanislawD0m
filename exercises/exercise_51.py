# Your solution to Exercise 51
# python -m unittest tests/test_exercise_51.py
a = int(input("Enter the first four-digit number: "))
b = int(input("Enter the second four-digit number: "))
for i in range(a, b):
    original_integer = i
    digit_thousands = original_integer % 10
    digit_hundreds = original_integer // 10 % 10
    digit_tens = original_integer // 100 % 10
    digit_units = original_integer // 1000
    if digit_thousands == digit_hundreds == digit_tens or \
       digit_thousands == digit_hundreds == digit_units or \
       digit_thousands == digit_tens == digit_units or \
       digit_hundreds == digit_tens == digit_units:
        print(i, end=" ")