# import csv
# from random import *

# 1 Сделать программу для записи и чтения из файла. При запуске программа запросит ввести имя файла. Расширение txt должно 'прилипнуть' автоматически.
# Также необходимо сделать 3 пункта меню:
#           1. Запись в файл (Данные будут браться с input и записываться в файл)
#           2. Чтение файла
#           3. Очистка файла

#
# name = input("Enter the name of file: ").title()
# B = print(f'{name}.txt')
#
# x = int(input("Select the mode: 1 - w, 2 - r, 3 - file cleanup: "))
# if x == 1:
#     with open("Short.txt", "w") as file:
#         words = input("write something: ")
#         file.write(words)
# if x == 2:
#     with open("Short.txt", "r") as file:
#         content = file.read()
#         print(content)
# if x == 3:
#     with open("Short.txt", "w") as file:
#         file.write(" ")


# 2 Сделать программу, которая будет генерировать список случайных чисел.
# Необходимо сделать запись этих чисел в CSV файл с двумя столбцами: Четные и нечётные, либо любое другое разделение
# (например положительные и отрицательные числа). (rec: DictWriter)


# Nums = [randint(0, 50) for i in range(0, 30)]
# print(Nums)
#
#
# with open('Nums.csv', 'w', newline='') as csvfile:
#     columns = ['odd', 'even']
#     writer = csv.DictWriter(csvfile, fieldnames=columns, delimiter=",")
#     writer.writeheader()
#     for i in Nums:
#         if i % 2 == 0:
#             writer.writerow({'odd': '---', 'even': i})
#         else:
#             writer.writerow({'odd': i, 'even': '---'})



#При помощи ф-ии filter отфильтровать из кортежа слов только те, которые являются палиндромами

wds = ['refer', 'tree', 'civic', 'radar', 'level', 'state', 'kayak', 'reviver', 'racecar']
print(list(filter(lambda wds: wds == wds[::-1], wds)))













