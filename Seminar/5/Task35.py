"""Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes """


n = int(input("Введите число: "))
def is_simple(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True
print(is_simple(n))