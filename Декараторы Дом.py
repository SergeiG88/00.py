# def my_decor(func):
#     def wrapper():
#         print('start')
#         func()
#         print('end')
#     return wrapper
#
# def my_func():
#     print('Тут основная функция')
#
#
# my = my_decor(my_func)
# # print(my)
# my()


# def my_decor(func):
#     def wrapper(n):
#         print('start')
#         func(n)
#         print('end')
#
#     return wrapper
#
# @my_decor
# def my_func(number):
#     print(number ** 2)
#
#
# my_func(10)

import time

def my_decor(func):
    def my_wr():
        start_time = time.time()
        func()
        print(time.time() - start_time)
    return my_wr()

@my_decor
def sp():
    spisok = [i ** 2 for i in range(100000) if i % 2 == 0]
    print(spisok)

# sp()
print(my_decor)


