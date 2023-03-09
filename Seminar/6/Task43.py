"""Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: 
1 2 3 2 3 
Вывод: 2
"""

import random
length_mass = int(input("Введите кол-во элементов списка: "))
random_mass = [random.randint(1,10) for _ in range(length_mass)]
print(random_mass)
count = 0
for i in random_mass:
    if random_mass.count(i) > 1:
        count +=1
print(count // 2)
print(random_mass)


"""my_list = [1, 1, 1, 2, 4, 2, 3, 4]
temp_list = []
for elem in my_list:
    count = my_list.count(elem)
    if count > 0 and elem not in temp_list:
        temp_list.append(elem)
        print(f"Элемент {elem} имеет пар {count // 2}")"""
