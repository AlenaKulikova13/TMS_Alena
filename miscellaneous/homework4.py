
#Задание на прошлую среду, которое не успела сделать.
# import random
# x = random.randint(1, 10)
# your_choice = int(input("Выберите число от 1 до 10: "))
# counter = 1
# while your_choice != x:
#     counter += 1
#     your_choice = int(input("Не то, угадывай: "))
# print(f"Угадал. Кол-во попыток {counter}")


#1 Создать функцию SumRange (start, end), которая будет суммировать все целые числа от start до end.
#  Дополнительно: Обработать следующий случай: Если пользователь задаст значение start больше, чем end, то они будут меняться местами.

# nums = list(range(1, 7))
# def sumRange(nums):
#     summa = sum(nums)
#     print(summa)
# sumRange(nums)


#2 Дано целое число. Создать функцию, которая будет возвращать сумму его цифр.

x = 3345
sum = 0
while(x > 0):
    sum = sum + x % 10
    x = x // 10
print(f"сумма цифр числа = {sum}")

#3 Дано целое число. Создать функцию, которая будет возвращать произведение его цифр.

# x = 3345
# mult = 1
# while (x > 1):
#     mult = mult * (x % 10)
#     x = x // 10
# print(f"произведение цифр числа = {mult}")


import datetime
currentdt = datetime.datetime.now()
print(currentdt)







