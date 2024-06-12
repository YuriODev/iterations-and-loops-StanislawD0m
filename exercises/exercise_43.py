# Your solution to Exercise 43
# python -m unittest tests/test_exercise_43.py
number = int(input("Enter the first integer: "))
first_largest, second_largest = number, 0
while number != 0:
    number = int(input(""))
    if number > first_largest:
        second_largest = first_largest
        first_largest = number
    elif number > second_largest:
        second_largest = number
print(second_largest)