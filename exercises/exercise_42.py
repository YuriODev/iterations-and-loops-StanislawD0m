# Your solution to Exercise 42
# python -m unittest tests/test_exercise_42.py
number = int(input("Enter the first number of the sequence: "))
count = 0
previous = number
while number != 0:
    number = int(input(""))
    if number < previous:
        count += 1
    previous = number
print(count)