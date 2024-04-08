# def create_operation(operation):
#     if operation == "add":
#         def add(x, y):
#             return x + y
#
#         return add  # возвращаем функцию, как объект!! Тут скобки не нужны
#     elif operation == "subtract":
#         def subtract(x, y):
#             return x - y
#
#         return subtract
#
#
# my_func_add = create_operation("add")
# print(my_func_add(1, 2))

# def create_operation(operation):
#     if operation == 2:
#         def add(x, y):
#             return x * y
#
#         return add  # возвращаем функцию, как объект!! Тут скобки не нужны
#     elif operation == 3:
#         def subtract(x, y):
#             return x // y
#
#         return subtract
#
# # my_numbers = [2, 3]
#
# create_operation()

# def create_operation(operation):
#     if operation == 'add':
#         def add(x, y):
#             return x * y
#
#         return add  # возвращаем функцию, как объект!! Тут скобки не нужны
#
#         def subtract(x, y):
#             return x / y
#
#
#         return subtract
#
# my_func_add = create_operation('add')
# print(my_func
# print(my_func_add(1,_add(2,3))
# my_func_add = create_operation('add')
# print(my_func_add(1,2))
# my_func_add = create_operation('add')2))



# Ucheba
def create_operation(operation):
    if operation == 'add':
        def add(x, y):
            return x * y
        return add # возвращаем функцию, как объект!! Тут скобки не нужны
    elif operation == "subtract":

        def subtract(x, y):
            try:
                result = x / y
            except ZeroDivisionError:
                return "Делить на ноль нельзя"
            return result
        return subtract


my_func_add = create_operation('add')
print(my_func_add(2,3))
a = create_operation('subtract')
print(a( 4, 2 ))






multiply = lambda x, y: x ** y
print(multiply(2, 4))

def multiply_def(x, y):
   return x ** y
print(multiply_def(2,4))


class Repeater:
   def __init__(self, a, b):
       self.a = a
       self.b = b

   def __call__(self):
       return self.a * self.b


repeat_five = Repeater( 2 , 4)
print(f'стороны: {repeat_five.a} и {repeat_five.b}')
print(f'площадь: {repeat_five()}')
