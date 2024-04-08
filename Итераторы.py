# class Family:
#
#     def __init__(self):
#         self.dad = 'Вадим'
#         self.mom = "Татьяна"
#         self.son = 'Алексей'
#         self.i = 0
#
#     def __iter__(self):
#             # обнуляем счетчик перед циклом
#        self.i = 0
#             # возращаем ссылку на себя  - я буду итератором!
#        return self
#
#     def __next__(self):
#             # а этот метод возвращает значения по требованиям python
#         self.i += 1
#         if self.i == 1:
#             return f'Папа - {self.dad}'
#         if self.i == 2:
#             return f'Мама - {self.mom}'
#         if self.i == 3:
#             return f'Я - {self.son}'
#         if self.i == 4:
#             return f'Счастливая семья : )'
#         raise StopIteration()  # признак того, что больше возращать нечего
#
# my_family = Family()
# print(my_family)
# for value in my_family:
#     print(value)

# То есть под капотом у for происходит как бы следующее
# try:
#     while True:
#         value = my_family.__next__()
#         print(value)
# except StopIteration:
#     pass

# Такой же алгоритм срабатывает при вычислении вхождения в последовательность - оператор in
# print('Я - Алексей' in my_family)


# def fibonacci(n):
#     result = []
#     a, b = 0, 1
#     for _ in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result
#
# fib = fibonacci
# for value in fibonacci(n=10):
#     print(value)


class Fibonacci:
    # Итератор последовательности Фибоначчии жо № элементов

    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a

fib_iterator = Fibonacci(n=10)
print(fib_iterator)
for value in fib_iterator:
    print(value)
print(13 in fib_iterator)
