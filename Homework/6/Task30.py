"""Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Ввод: 7 2 5
Вывод: 7 9 11 13 15"""



a1 = int (input("Введите первый элемент прогрессии: "))
step = int (input("Введите шаг прогрессии: "))
count = int (input("Введите количество элементов в прогрессии: "))

print([i for i in range(a1, count*step+a1, step)])