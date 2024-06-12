# Your solution to Exercise 
# python -m unittest tests/test_exercise_26.py
n = int(input())
total = 0
for i in range(1,1000) :
    while i // 100 + (i % 100) // 10 + i % 10 == n :
        total += 1
print(total)