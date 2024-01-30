# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = [x * 3 for x in my_numbers if x % 2]
# # cp.map(lambda x : x * 3, filter(lambda x: x % 2, my_numbers))
# print(result)

# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
# result = [x *y for x in my_numbers for y in they_numbers]
# print(result)
# result = [x *y for x in my_numbers for y in they_numbers if x % 2]
# print(result)
# result = [x *y for x in my_numbers for y in they_numbers if x % 2 and y // 2]
# print(result)


# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = {x for x in my_numbers}
# print(result)


# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = {x for x in my_numbers}
# print(result, type(result))


# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = {x: x ** 2 for x in my_numbers}
# print(result, type(result))


# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = (x ** 1000 for x in my_numbers)
# print(result, type(result))
# for elem in result:
#     print(elem)


# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = (x ** 1000 for x in my_numbers)
# print(result, type(result))
# for elem in result:
#     print(elem)
# print('Еще разок')
# for elem in result:
#     print(elem)


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = (x ** 300000 for x in my_numbers)
for i in result:
    print(i)
    if str(i).startswith('100'):
        break TypeError