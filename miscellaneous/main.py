
# ("hello", "world" ,"!" ,sep=" " ,end="\n" ,file=file ,flush=True)
# file.close()
#
#
# #A = input("Tell me your favourite song:")
#
# Num1 = 4
# Num2 = 4
# print(id(Num1), id(Num1))
#
# Num3 = 74
# Num4 = str(74)
# print(id(Num3))
# print(id(Num4))
# file = open
# print("file1.txt","a+")
# file.close()
#
# A = 8
# B = 8
# C = 8
#
# print(id(A))
# print(id(B))
# print(id(C))
#
# D = [1, 2, 3]
# E = [1, 2, 3]
# print(id(D), id(E))
#
# D = (1, 2, 3)
# E = (1, 2, 3)
# print(id(D), id(E))
#
#
# A = str(8)
# B = bool(8)


# while(True):
#     i = input("Имя: ")
#     x = int(input("Возраст: "))
#     if x <= 18:
#         print(f"Привет, {i}!")
#     if x <=30:
#         print(f"Здравствуй, {i}!")
#     if x >= 30:
#         print(f"Здравствуйте, {i}!")


# import random
# x = random.randint(1, 10)
# your_choice = int(input("Выберите число от 1 до 10: "))
# counter = 1
# while your_choice != x:
#     counter += 1
#     your_choice = int(input("Не то, угадывай: "))
# print(f"Угадал. Кол-во попыток {counter}")

# import datetime
# currentdt = datetime.datetime.now()
# print(currentdt)


# def Line(function_to_decorate):
#     def wrapper():
#         print("Я иду первым.")
#         function_to_decorate()
#         print("Я второй.")
#     return wrapper
#
# def Good_person():
#     print("Мне только спросить!")
#
# Good_person_decorated = Line(Good_person)
# Good_person_decorated()


# def Songs(to_be_decorated):
#     def wrapper():
#         print("Послушаем эту")
#         to_be_decorated()
#         print("А потом эту")
#     return wrapper
#
# def no_music_taste():
#     print("Ой, переключи")
#
# no_music_taste_decorated = Songs(no_music_taste)
# no_music_taste_decorated()


# A = [1, 7, 9]
# new_A = list(map(int, A))


# def talk():
#     def whisper(word = "да"):
#         return word.lower()+"...";
#     print(whisper())
# #
# talk()
#
# def getTalk(type = "shout"):
#     def shout(word = "да"):
#         return word.capitalize() + "!"
#
#     def whisper (word = "да"):
#         return word.lower() + "...";

#     if type == "shout":
#         return shout
#     else:
#         return whisper
#
#
# talk = getTalk
#
# print(talk)
#
# print(getTalk("whisper")())
#
#
# def doSomethingBefore(func):
#     print("я делаю что-то еще перед тем как вызвать функцию, которую ты мне передал")
#     print(func())
#
# doSomethingBefore(scream)


# def my_shiny_new_decorator(a_function_to_decorate):
#
#     def wrapper_around_original_function():
#         print("я код, работающий до вызова функции")
#
#         a_function_to_decorate()
#
#         print("а я код, работающий после")
#
#     return wrapper_around_original_function
#
# def a_stand_alone_function():
#     print("я просто одинокая функция, не трогай")
#
# # a_stand_alone_function()
#
# a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
# a_stand_alone_function_decorated()
#
# a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
# a_stand_alone_function()

#
# @my_shiny_new_decorator
# def another_stand_alone_function():
#     print("оставь меня в покое")
#
# another_stand_alone_function()
#
# another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_fucntion)
