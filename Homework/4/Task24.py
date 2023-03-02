"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
различное число ягод – на i-ом кусте выросло РАНДОМНОЕ колличество ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки."""


"""import random
n = int(input("Введите количество кустов: "))
bush = list()
for i in range(n):
    x = int(input("Введите количество ягод на каждом кусте: "))
    bush.append(x)

sum_berries = list()
for i in range(len(bush)-1):
    sum_berries.append(bush[i-1]+bush[i]+bush[i+1])
sum_berries.append(bush[-2]+bush[-1]+bush[0])  
print(max(sum_berries))
"""


import random
amount_bush = int (input("Введите количество кустов: "))
max_sum = 0
list_1 = [random.randint(1, 10) for _ in range(amount_bush)]
print(list_1)
for number_bush in range(amount_bush):
    if number_bush == 1:
        max_berries = list_1[-1] + sum(list_1[:2])
    elif number_bush == len(list_1):
        max_berries = sum(list_1[amount_bush-2:])+list_1[0]
    else:
        max_berries = sum(list_1[number_bush-2:number_bush+1])
    if max_berries > max_sum:
        max_sum = max_berries
print(f"максимальное количество ягод равно {max_sum}")
