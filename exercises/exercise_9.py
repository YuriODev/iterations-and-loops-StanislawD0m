# Your solution to Exercise 9
# python -m unittest tests/test_exercise_9.py
a = int(input())
b = int(input())
c = int(input())
for i in range(a,b + 1) :
    if i % c != 0 :
        continue
    print(i , end = " ")
    