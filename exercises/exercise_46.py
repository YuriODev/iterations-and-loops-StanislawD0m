# Your solution to Exercise 46
# python -m unittest tests/test_exercise_46.py
number = int(input("Enter a natural number: "))
digit = int(input("Enter a digit: "))
position = 0
while number > 0:
    last_digit = number % 10
    position += 1
    if last_digit == digit:
        print(position)
        break
    number //= 10
if number == 0:
    print(0)