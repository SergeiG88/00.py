# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого
# объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#    - Тип объекта.
#    - Атрибуты объекта.
#    - Методы объекта.
#    - Модуль, к которому объект принадлежит.
#    - Другие интересные свойства объекта, учитывая его тип (по желанию).
#
#
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
# {'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}
#
import inspect


# def introspection_info(obj):
#     attributes = []
#     methods = []
#     print(dir(obj))
#     for el in dir(obj):
#         print([el, getattr(obj,el)])
#         if callable(getattr(obj,el)):
#             methods.append(el)
#         else:
#             attributes.append(el)
#     return {
#         f'type:{type(obj).__name__}, '
#         f'attributes and methods:{dir(obj)}, '
#         f'module:{__name__}'
#     }
#
#
# number_info = introspection_info(42)
# print(number_info)

# inspect get module


# def introspection_info(obj):
#     attributes = []
#     methods = []
#     print(dir(obj))
#     for el in dir(obj):
#         print([el, getattr(obj,el)])
#         if callable(getattr(obj,el)):
#             methods.append(el)
#         else:
#             attributes.append(el)
#     return {
#         f'type:{type(obj).__name__}, '
#         f'attributes and methods:{dir(obj)}, '
#         f'module:{type(obj).__name__}'
#     }
#
#
# number_info = introspection_info(42)
# print(number_info)

import inspect
from random import randint
def introspection_info(obj):
    attributes = []
    methods = []
    for atr in dir(obj):

        if callable(getattr(obj, atr)):
            methods.append(atr)
        else:
            attributes.append(atr)
    modul = inspect.getmodule(randint).__name__ if inspect.getmodule(obj) else '__main'
    return  {'type(obj': type(obj).__name__, 'attributes': attributes, 'methods': methods, 'modul': modul}



number_info = introspection_info(42)
print(number_info)




















#
#
# import requests
# from pprint import pprint
#
# some_string = 'i am a string'
# some_number = 42
# some_list = [some_string, some_number]
#
# def some_function(param, param_2='n/a'):
#     print('my params is, param, param_2')
#
#
#
# class SomeClass:
#     def __init__(self):
#         self.attribute_1 = 27
#
#
#
#     def some_class_method(self, value):
#         self.attribute_1 = value
#         print(self.attribute_1)
#
# some_object = SomeClass()
#
# for attr_name in dir(requests):
#     attr = getattr(requests, attr_name)
#     print(attr_name, type(attr))

# print(hasattr(requests, 'get'))
# http_get = getattr(requests,'get')
# print(type(http_get))

# pprint(dir(requests))

# Встроенная функция hasattr() - проверка на существования атрибута
# print(hasattr(some_object, 'attribute_1'))
# print(hasattr(some_object, 'attribute_1'))
# Встроенная функция getattr - получение атрибута
# print(getattr(some_object, 'attribute_1'))
# print(some_object.attribute_1)
# print(getattr(some_object, 'attribute_2', 'значение, если атрибута нет'))



# pprint(dir(some_number))
# pprint(dir(some_list))
# pprint(dir(some_function))
# pprint(dir(SomeClass))
# pprint(dir(some_object))

# func = some_function
#
# print(func.__name__)
# print(__name__)
# print(type(some_list))
# print(type(some_list) is int)
# print(type(some_list) is list)
# print(type(requests))

# rq = requests
#
# def check_param(value):
#     if type(value) is str:
#         print('Обрабатываем строку', value)
#     else:
#         print('Это не строка')
#
# check_param(value=some_string)
# check_param(value=some_list)








# number_info = introspection_info(42)
# print(number_info)





















