"""Задача 16: Требуется вычислить, сколько раз встречается
некоторое число X в массиве A[1..N]. Пользователь в первой строке 
вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    3
    -> 1"""

from random import randint
A = int (input("Введите количество элементов массива: "))
numbers = []
for i in range(A):
    numbers.append(randint(1, A))
print (numbers)


b = int (input("Введите искомое число: "))
count = 0
for i in range(A):
    if numbers[i] == b:
        count +=1
print(count)



#print(f'Number of "{my_number}" in mass = {random_mass.count(my_number)}') вариант поиска 