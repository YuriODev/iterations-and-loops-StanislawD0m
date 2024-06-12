# Your solution to Exercise 4
#python -m unittest tests/test_exercise_4.py
n = int(input())
hash_num = 1
for i in range(n):
    print(str(hash_num) , hash_num * "#")
    hash_num += 1