# def get_russian_names():
#     return ['Ваня', 'Коля', 'Маша']
#
# # Имя функции указывает на объект функции. Обычная переменная
# print(type(get_russian_names))
# # можно узнать функции
# print(get_russian_names.__name__)
#
# my_func = get_russian_names
# print(my_func())
# # название останется как при определении
# print(my_func.__name__)


# def get_russian_names():
#     return ['Ваня', 'Коля', 'Маша', ]
#
# def get_british_names():
#     return ['Oliver', 'Jack', 'Harry', ]
#
# name_getters = [get_russian_names, get_british_names]
# for name_getter in name_getters:
#     print(name_getter())


# def get_russian_names():
#     return ['Ваня', 'Коля', 'Маша', ]
#
# def get_british_names():
#     return ['Oliver', 'Jack', 'Harry', ]
#
# def print_names(message, name_getter):
#     print(message, name_getter())
#
# print_names(message='Русские имена', name_getter= get_russian_names)


# def get_russian_names():
#     return ['Ваня', 'Коля', 'Маша', ]
#
# def get_british_names():
#     return ['Oliver', 'Jack', 'Harry', ]
#
# def print_names(message, name_getter):
#     print(message, name_getter())
#
# names = {'Русские имена': get_russian_names, 'Английские имена': get_british_names}
# for message, name_getter in names.items():
#     print_names(message, name_getter)


def adder(*args):
    res = 0
    for number in args:
        res += number
    return res

def multiplier(*args):
    res = 1
    for number in args:
        res += number
    return res

def process_numbers(numbers, handler):
    result = handler(*numbers)
    print(f'Получилось {result}')

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
process_numbers(numbers=my_numbers, handler=adder)
process_numbers(numbers=my_numbers, handler=multiplier)