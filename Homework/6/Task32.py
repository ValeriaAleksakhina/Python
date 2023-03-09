"""Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]

Вывод: [1, 9, 13, 14, 19]"""

import random
count_list = int(input("Введите количество элементов списка: "))
list = [random.randint(-10,10) for _ in range(count_list)]
print(list)

min = int(input("Введите минимум диапазона: "))
max = int(input("Введите максимум диапазона: "))

list_index = []
for i in range(count_list):
    if min<=list[i] and max>=list[i]:
        list_index.append(i)
print(list_index)