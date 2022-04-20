

Nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# New_list = filter(lambda x: x % 3 == 0, Nums)
# print(list(New_list))

def func(Nums):
    '''
    Функция возвращает числа, кратные 3-м
    '''
    for i in Nums:
        if i % 3 == 0:
            print(i)
func(Nums)

print(func.__doc__)

