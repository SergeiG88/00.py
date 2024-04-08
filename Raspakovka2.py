def print_params(a, b, c):
    return (a, b, c)

values_list = [1, 'строка', True]
values_dict = {'a': 2, 'b': 'qwerty', 'c': 4}
#values_list2 = [2, 42]
param = print_params(*values_list, **values_dict)
print(param)










