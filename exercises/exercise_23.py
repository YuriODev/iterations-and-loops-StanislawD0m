# Your solution to Exercise 23
# python -m unittest tests/test_exercise_23.py
total = 0
sum = 0
num = int(input())
while num > 0 :
    total += 1
    sum += num
    num = int(input())
if sum != 0 or total != 0 :
    average = sum / total 
    print(average)
else:
    print(0)