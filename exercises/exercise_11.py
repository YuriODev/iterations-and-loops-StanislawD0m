# Your solution to Exercise 11
# python -m unittest tests/test_exercise_11.py
n = int(input())
total = 0
for i in range(1,n+1): 
    total += i/(i + 1)
print(f"{total:.2f}")
