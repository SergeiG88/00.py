# # -*- coding: utf-8 -*-
#
# # Декораторы - это просто.
#
# # Предположим есть функция с тяжеловесными вычислениями:
# # найти количество цифр в произведении 5000-х степеней чисел
#
#
# # def digits(*args):
# #     total = 1
# #     for number in args:
# #         total *= number ** 5000
# #     return len(str(total))
# #
# #
# # # и нам надо засечь время выполнения функции
# # import time
# # started_at = time.time()
# # result = digits(3141, 5926, 2718, 2818)
# # print(result)
# # ended_at = time.time()
# # elapsed = round(ended_at - started_at, 4)
# # print(f'Функция работала {elapsed} секунд(ы)')
#
#
# # Вообще, учет времени выполнения - достаточно типичная ситуация, и хочется сделать функцию-помощника
# #
# # Напишем функцию высшего порядка, на вход которой передается другая функция и параметры с которыми надо её вызвать
# # def time_track(func, *args, **kwargs):
# #     started_at = time.time()
# #
# #     result = func(*args, **kwargs)
# #
# #     ended_at = time.time()
# #     elapsed = round(ended_at - started_at, 4)
# #     print(f'Функция работала {elapsed} секунд(ы)')
# #     return result
# #
# #
# # def digits(*args):
# #     total = 1
# #     for number in args:
# #         total *= number ** 5000
# #     return len(str(total))
# #
# #
# # result = time_track(digits, 3141, 5926, 2718, 2818)
# # print(result)
#
#
# # Но можно пойти еще глубже - пусть time_track еще и возвращает функцию.
# # Функцию, которая заместит оригинальную func.
# # def time_track(func):
# #     def surrogate(*args, **kwargs):
# #         started_at = time.time()
# #
# #         result = func(*args, **kwargs)
# #
# #         ended_at = time.time()
# #         elapsed = round(ended_at - started_at, 4)
# #         print(f'Функция работала {elapsed} секунд(ы)')
# #         return result
# #     return surrogate
# import time
#
# def digits(*args):
#     total = 1
#     for number in args:
#         total *= number ** 5000
#     return len(str(total))
#
#
# timed_digits = time_track(digits)
# result = timed_digits(3141, 5926, 2718, 2818)
# print(result)
#
# # а можно вообще сделать так
# # digits = time_track(digits)
# # result = digits(3141, 5926, 2718, 2818)
# # print(result)
# # и теперь digits - почти та же функция, но не та. Она отдекорирована функцией time_track
# # за счет *args, **kwargs внутренняя surrogate принимает все параметры
# # и тут же передает их в декорируемую функцию
#
#
# # в пайтон есть синтаксический сахар для декораторов. выглядит он так
# @time_track
# def digits(*args):
#     total = 1
#     for number in args:
#         total *= number ** 5000
#     return len(str(total))
#
# # Это аналог digits = time_track(digits)
#
# # Минусы декораторов:
# #  - затруднена отладка
# #  - нужно делать определенные действия, что бы сохранить аттрибуты декорерируемой функции (см functools.wraps)
#
#
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
# my_func(10)
#
# # def my_decor(func):
# #     def my_wr():
# #         start_time = time.time()
# #         func()
# #         print(time.time() - start_time)
# #     return my_wr()
# #
# # @my_decor
# # def sp():
# #     spisok = [i ** 2 for i in range(100000) if i % 2 == 0]
# #     print(spisok)
# #
# # sp()
# # print(my_decor)
#
# # def my_decor(func):
# #     def wrapper():
# #         print('start')
# #         func()
# #         print('end')
# #     return wrapper
# #
# # def my_func():
# #     print('Тут основная функция')
# #
# #
# # my = my_decor(my_func)
# # # print(my)
# # my()
#
#
# # def my_decor(func):
# #     def wrapper(n):
# #         print('start')
# #         func(n)
# #         print('end')
# #
# #     return wrapper
# #
# # @my_decor
# # def my_func(number):
# #     print(number ** 2)
# #
# #
# # my_func(10)
#
# import time
#
# # def my_decor(func):
# #     def my_wr():
# #         start_time = time.time()
# #         func()
# #         print(time.time() - start_time)
# #     return my_wr()
# #
# # @my_decor
# # def sp():
# #     spisok = [i ** 2 for i in range(100000) if i % 2 == 0]
# #     print(spisok)
# #
# # # sp()
# # print(my_decor)
#
#
# import time
#
# import threading
#
# def print_numbers():
#     for i in range(10):
#         print(i)
#
# def print_letters():
#     for letter in 'abcdefghij':
#         print(letter)
#
# # Создаем потоки
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
# # Запускаем потоки
# thread1.start()
# thread2.start()
#
# # Ждем завершения потоков
# thread1.join()
# thread2.join()


# import threading
# import time
#
#
# def print_hello():
#     for i in range(4):
#         time.sleep(0.5)
#         print("Hello")
#
#
# def print_hi():
#     for i in range(4):
#         time.sleep(0.7)
#         print("Hi")
#
#
# t1 = threading.Thread(target=print_hello)
# t2 = threading.Thread(target=print_hi)
# t1.start()
# t2.start()

import threading
import time

class MyClass:

    def __init__(self):
        self._thread = threading.Thread(target=self.run)
        self._thread.start()

    def run(self):
        for i in range(5):
            print('worker thread', i)
            time.sleep(.5)

    def join(self):
        self._thread.join()

my_obj = MyClass()
for i in range(12):
    print('main thread', i)
    time.sleep(.5)
my_obj.join()
print('done')