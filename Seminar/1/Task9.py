"""2. Напишите программу, которая будет принимать на вход дробь
 и показывать первую цифру дробной части числа.
    
    *Примеры:*
    
    - 6,78 -> 7
    - 5 -> нет
    - 0,34 -> 3"""

n = float(input("Введите число: "))
print(int(n*10)%10)
