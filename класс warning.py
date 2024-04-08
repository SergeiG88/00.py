# import warnings
#
# def greet_person(person_name):
#     if person_name == 'Robert':
#         warnings.warn('Опять этот Роберт....')
#         print(f'Hi there {person_name}')
#
# greet_person('Robert')
# print('Выполнение продолжается')
# for i in range(10):
#     print(f'i={i}')

# import warnings
#
# def greet_person(person_name):
#     if person_name == 'Robert':
#         warnings.warn('Опять этот Роберт....', category=RuntimeWarning)
#         print(f'Hi there {person_name}')
#
# greet_person('Robert')
# print('Выполнение продолжается')
# for i in range(10):
#     print(f'i={i}')


import warnings

def greet_person(person_name):
    if person_name == 'Robert':
        warnings.warn('Опять этот Роберт....', category=RuntimeWarning)
        print(f'Hi there {person_name}')

warnings.simplefilter('ignore')
# warnings.simplefilter('error')
# greet_person('Robert')
try:
    greet_person('Robert')
    print('Выполнение продолжается')
except RuntimeWarning:
    print('поймали RuntimeWarning')
for i in range(10):
    print(f'i={i}')

# import warnings
#
# def greet_person(person_name):
#     if person_name == 'Robert':
#         warnings.warn('Опять этот Роберт....', category=RuntimeWarning)
#         print(f'Hi there {person_name}')
#
# # warnings.simplefilter('ignore')
# warnings.simplefilter('error')
#
# try:
#     greet_person('Robert')
#     print('Выполнение продолжается')
# except RuntimeWarning:
#     print('поймали RuntimeWarning')
# for i in range(10):
#     print(f'i={i}')