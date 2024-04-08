def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2
    elif n == 3:
        def multiplier(x):
            return x / 3
    else:
        raise Exception('Я смогу сделать умножители только на 2 или 3')

    return multiplier

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

by_2 = get_multiplier_v1(n=2)
by_3 = get_multiplier_v1(n=3)
result = map(by_2, my_numbers)
print(list(result))
result = map(by_3, my_numbers)
print(list(result))


# def get_multiplier_v2(n):
#
#     def multiplier(x):
#         return x * n
#
#     return multiplier
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# by_5 = get_multiplier_v2(n=5)
# print(by_5(x=42))
#
# result = map(by_5, my_numbers)
# print(list(result))
#
# by_100 = get_multiplier_v2(100)
# result = map(by_100, my_numbers)
# print(list(result))


# from pprint import pprint
#
# def matrix(some_list):
#
#     def multiply_colum(x):
#         res = []
#         for element in some_list:
#             res.append(element * x)
#         return res
#
#     return multiply_colum
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# matrix_on_my_numbers = matrix(some_list=my_numbers)
# print(matrix_on_my_numbers(x=100))
# my_numbers.append(42)
# print(matrix_on_my_numbers(x=100))
#
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
# result = map(matrix_on_my_numbers, they_numbers)
# pprint(list(result))
#
# my_numbers.extend([10, 20, 30])
# result = map(matrix_on_my_numbers, they_numbers)
# pprint(list(result))


# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = map(lambda x: x + 10, my_numbers)
# print(list(result))
#
# my_func = lambda x: x + 10
# print(my_func(x=42))
# print(type(my_func))


# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
# result = map(lambda x, y: x + y, my_numbers, they_numbers)
# print(list(result))



