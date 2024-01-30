# import warnings
#
# def function_with_warning(person_name):
#     if person_name == 'Robert':
#         warnings.warn( 'Это важное предупреждение', UserWarning)
#     print(f'Предупреждение было перехвачено как исключение: {person_name}')
#
# warnings.simplefilter('error')
# function_with_warning('Robert')
# # Пример 1: Фильтр установлен в 'error'
# try:
#     function_with_warning('Robert')
#     print('Пример 1: Фильтр "error"')
# except UserWarning as e:
#     print(f'поймали UserWarning: {e}')
# for i in range(1):
#     print('0.01')


# import warnings
#
# def function_with_warning(person_name):
#     if person_name == 'Robert':
#         warnings.warn( 'Это важное предупреждение', UserWarning)
#     print(f'Предупреждение было перехвачено как исключение: {person_name}')
#
# warnings.simplefilter('ignore')
# function_with_warning('Robert')
# # Пример 2: Фильтр установлен в 'ignore'
# try:
#     function_with_warning('Robert')
#     print('Пример 2: Фильтр "ignore"')
# except UserWarning as e:
#     print(f'поймали UserWarning: {e}')
# for i in range(2):
#     print('0.01')



# import warnings
#
# def function_with_warning(person_name):
#     if person_name == 'Robert':
#         warnings.warn( 'Это важное предупреждение', UserWarning)
#     print(f'Предупреждение было перехвачено как исключение: {person_name}')
#
# # warnings.simplefilter('always')
# # function_with_warning('Robert')
# # Пример 2: Фильтр установлен в 'always'
# try:
#     function_with_warning('Robert')
#     print('Пример 2: Фильтр "always"')
# except UserWarning as e:
#     print(f'поймали UserWarning: {e}')
# for i in range(2):
#     print('0.01')

import warnings

# def function_with_warning(numb_1):
#     print('Перед генерацией предупреждения')
#     # if numb_1 == '0.01':
#     warnings.warn( 'Это важное предупреждение', category=RuntimeWarning)
#     print('Предупреждение генерации')
# warnings.simplefilter('error')
# try:
#     # function_with_warning('numb_1')
#     print('После генерации предупреждения')
#     2/0.01
#     # print('ч')
# except RuntimeWarning as e:
#     print(f'Предупреждение было перехвачено как исключение {e}')

def function_with_warning(numb_1):
    print('Перед генерацией предупреждения')
    # if numb_1 == '0.01':
    warnings.warn( 'Это важное предупреждение', category=RuntimeWarning)
    print('Предупреждение генерации')
warnings.simplefilter('error')
try:
    for i in range(3):
        print(3/0)
    2/0.01
    # print('ч')
except ZeroDivisionError as e:
    print(f'Предупреждение было перехвачено как исключение {e}')
























    # for i in range(type(int 0.01)):
    # for i in range(0):
    #     print(f'i={i}')

# warnings.simplefilter( 'error', UserWarning)
# function_with_warning()
#     print('\n')


# # Пример 2: Фильтр установлен 'default'
# print('Пример 1: Фильтр "default"')
# warnings.simplefilter( 'default', UserWarning)
# function_with_warning()