"""Задача №23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
Примечание: Пользователь может вводить значения
списка или список задан изначально."""

a = [0, -1, 5, 2, 3]
count = 0
for i in range(len(a)-1):
    if a[i+1] > a[i]:
        count += 1
print(count)
