# Your solution to Exercise 7
# python -m unittest tests/test_exercise_7.py
n = int(input())
space_num = 0
for i in range(n) :
    print("#" + space_num   * " " + "#")
    space_num += 1
