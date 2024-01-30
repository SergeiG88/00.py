# try:
#     i = 0
#     print(10 / i)
#     print('сделано')
# except:
#     # ловим все ошибки
#     print('нельзя делить на ноль')


# try:
#     truba = a + b
#     truba = 10/0
# except (ZeroDivisionError, NameError): # указываем имена классов
#      print('что то пошло не так, но мы устояли')


# try:
#     truba = a + b
#     truba = 10/0
# except ZeroDivisionError:
#      print('они убили кенни - хотели делить на ноль')
# except NameError:
#     print('нет такой переменной')


# try:
#     a = 10/0
# except ZeroDivisionError as exc:
#      print(f'вот что пошло не так - {exc}, но сы еще на плаву')


# try:
#     truba = a + b
# except (ZeroDivisionError, NameError) as exc:
#      print(f'вот что пошло не так - {exc}, но сы еще на плаву')


def f1(number):
    return 10 / number


def f2():
    sum = 0
    for i in range(2, -1, -1)
        sum += f1(number=1)
        print(sum)

total = f2()
try:

except ZeroDivisionError as exc:
    print(f'вот что пошло не так - {exc}, но мы устояли')