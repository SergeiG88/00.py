# def f(x):
#     return x ** 2
# a = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
# b = list(map(f, a))
# print(b)
#
#
#
# def f(x):
#     return x%2==1
# a = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
# b = list(filter(f, a))
# print(b)
# #
#

#

def f(x):
    return x ** 2
a = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
b = list(map(lambda x: x**2, filter(lambda x: x%2 !=0, a)))
print(b)
