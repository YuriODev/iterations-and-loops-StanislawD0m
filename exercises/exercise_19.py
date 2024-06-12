# Your solution to Exercise 19
# python -m unittest tests/test_exercise_19.py
n = int(input())
for i in range(10,100):
    sum_of_squares = (i // 10) ** 2 + (i % 10) ** 2
    if sum_of_squares % n == 0:
        print(i ,end = ", ")
print()