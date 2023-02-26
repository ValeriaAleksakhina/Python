"""Задача 18: Требуется найти в массиве A[1..N] 
самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число
N – количество элементов в массиве. В последующих 
строках записаны N целых чисел Ai.
Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    6
    -> 5"""

from random import randint
A = int (input("Введите количество элементов массива: "))
numbers = []
for i in range(A):
    numbers.append(randint(1, A))
print (numbers)

x = int (input("Введите число, которое требуется сравнить: "))
find_num = numbers[0]
for i in numbers:
    if abs(i - x) < abs(find_num - x):
        find_num = i
print(find_num)
       