"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть"""

import random
n = int(input("Введите количество монеток: "))
count_orel = 0
count_reshka = 0
for i in range(n):
    x = random.randint(0, 1)
    print (f"сторонa {i+1} = {x}")
    if x == 0:
        count_orel += 1
    else:
        count_reshka += 1
if count_reshka > count_orel:
    print(count_orel)
else:
    print(count_reshka)


