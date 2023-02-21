"""Задача No11. Решение в группах
Дано натуральное число A > 1. 
Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что φ(n)=A. 
Если А не является числом Фибоначчи, выведите число -1.
Input: 5 Output: 6
15 минут"""

n = int (input("Введите число: "))
i = 2
a = 0 # Сумма двух предыдущих
b = 0 # первое число
c = 1 # второе число

while a < n:
    a = b + c
    b = c
    c = a
    i +=1
    
    if a > n:
        i = 0
if i == 0:
    print("-1")
else:
    print(i)


