"""Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()"""

first = 'a a a b c a a d c d d'
second = first.split()
third = []
for i in range(len(second)):
  if second[:i+1].count(second[i]) == 1:
    third.append(second[i])
  else:
    third.append(second[i] + '_' + str(second[:i].count(second[i])))
print(third)



"""first = 'a a a b c a a d c d d'
second = first.split()
for i in range(len(second)):
  if second[:- i - 1].count(second[- i - 1]) >= 1:
    second[- i - 1] = second[- i - 1] + '_' + str(second[:- i - 1].count(second[- i - 1]))
print(second)"""