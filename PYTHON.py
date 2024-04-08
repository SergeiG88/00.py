# num = int(input('Введите значеrние: '))
# num2 = int(input('Введите значение: '))
# sum = num + num2
# print('Результат', sum)
from os import name


# n = 10
# if n > 9:
#     print(f'верно {n} больше 9')
# else:
#     print(f'{n} меньше 5')


# number = int(input('Введите значеrние: '))
#
# if number > 19: # if - если
#     print('положительное число')
# elif number == 0: # если number равен нулю
#     print('равно нулю') # распечатай
# else: # иначе
#     print('отрицательное число')

# animals = ['кошка', 'собака', 'лошадь', 'черепаха']
# for animal in animals:
#     print('привет ' + animal)

# student_name = 'тимур'
# student_list = ['саша', 'таня', 'настя','тимур']
# for student in student_list:
#     if student == student_name:
#         print(f'студент {student_name} найден')
#         break # остановка цикла
#     else:
#         print(f'студент {student_name} не найден')

# n = 10 # объявление переменной
# summa = 0 # объявление переменной
# i = 1 # объявление переменной
# while i <= n: # до тех пор, пока i = n
#     summa = summa + i # пока условие верно, при каждой итерации цикла, к значению переменной summa, добавляем i
#     i = i +1 # счетчик количества итераций
# print('переменная сумма равна: ', summa, 'счетчик равен: ', i)

# for i in 'string':
#     if i == 'n':
#         break
#     print(i)
# print('i равен символу n, завершаем цикл')

# for i in 'string':
#     if i == 's':
#         continue
#     print(i)
# print('i равен символу s, конец цикла')

# list = ['вася', 'дима', 'настя', 'кирилл']
# for i in list:
# pass

# import random
#
# count = 0
# x = random.randint(1, 100)
# counter = 0
# print("Попробуй отгадать загаданное мной число")
# print("Как тебя зовут?")
# player = input()
# print(player)
# while count != x:
#     count = int(input(str(player) + " введи число:\n"))
#     counter = counter + 1
#     if count > x:
#         print("Число должно быть меньше")
#     elif count < x:
#         print("Число должно быть больше")
#     else:
#         print("Вы угадали загаданное число за " + str(counter) + " попыток")
#         break

# def hello(name):#
#
# # Эта функция приветствия.
# # Аргумент name передается в качестве параметра
#
#     print('Привет, " + name + " Доброе утро')
# hello()

# def hello(name):
#
#
#     print("Привет, " + name + " Доброе утро")
#
# hello("Тимур")

# def value(number):
# # Возвращаем значение введенного числа
#     if number >= 0:
#         return number
#     else:
#         return -number
# print(value(2))
# print(value(-4))

# def testfunc():
#     x = 10
#
#     print("Значение внутри функции: ", x)
#
#
# x = 20
#
# testfunc()
#
# # print("Значение переменной за пределами функции: ", x)

# def func(name, message):
# # """
# # # Эта функция принимает две переменные
# # # name и message
# # """
#
#     print("Привет", name + ', ' + message)
#
# func("Тимур", "Доброе утро")

# def hello(name, message="Доброе утро"):
#     print("Hello", name + ', ' + message)
#
# hello("Тимур")
#
# hello("Мария", "Как дела?")

# def hello(*names):
#
# # """ Пример функции с передачей
# #
# # неограниченного количества аргументов"""
#
#     for i in names:
#         print("Привет", i)
#
# hello("Тимур", "Павел", "Настя", "Василий", "Женя")

def make_negative( number ):
    return number
print(make_negative(-1))
print(make_negative(-5))