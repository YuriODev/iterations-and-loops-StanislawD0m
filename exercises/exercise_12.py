# Your solution to Exercise 12
#python -m unittest tests/test_exercise_12.py
n = int(input())
total = 0
for i in range(100,1000) :
        if i % n == 0:
            total += i
print(total)