"""*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость
введенного пользователем слова. Будем считать, что на вход подается 
только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*
ноутбук
    12"""

dict = {1:'AEIOULNSTRАВЕИНОРСТ',
      	2:'DGДКЛМПУ',
      	3:'BCMPБГЁЬЯ',
      	4:'FHVWYЙЫ',
      	5:'KЖЗХЦЧ',
      	8:'JZШЭЮ',
      	10:'QZФЩЪ'}



word = input('Введите слово: ').upper()
print(sum([key for i in word for key, value in dict.items() if i in value]), 'очков') 

# 2 способ

"""count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count)
"""


# 3 способ

'''word = input('Введите слово: ')
count = 0
for i in word:
    for key, element in dictionary.items():
        if i.upper() in element:
            count += key
print (f"слово имеет {count} очков")'''