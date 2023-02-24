"""Задача 17. Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6"""

"""from random import randint

numbers = []
for i in range(10):
    numbers.append(randint(-10, 10))
print (numbers)

count = 0"""

a = [1, 1, 2, 0, -1, 3, 4, 4]
a = set(a)
print (len(a))