
#2
#
# A = 13
# B = 13
# if id(A) == id(B):
#     print("A == B")
# A = (bool(A))
# B = (str(B))
# print(id(A))
# print(id(B))
#
#
# 3 with unspecified number
#
# x = int(input("Введите число: "))
# y = int(input("Выберите СС: 1 - двоичная; 2 - восьмеричная; 3 - шестандцатеричная: "))
# if y == 1:
#     print(bin(x))
# elif y == 2:
#     print(oct(x))
# elif y == 3:
#     print(hex(x))
# else:
#     pass

# 3 with specified number

# file = open("Homework_2.txt","w")
#
# x = 9
# print(f"Десятичное {x} --> Двоичное",bin(x), file=file)
# print(f"Десятичное {x} --> Восьмеричное",oct(x), file=file)
# print(f"Десятичное {x} --> Шестнадцатеричное",hex(x), file=file)
#
# file.close()



def Generator (a : int, b : int, c : int) -> list:
    return [i for i in range (a, b, c)]
print(Generator(15, 20, 2))