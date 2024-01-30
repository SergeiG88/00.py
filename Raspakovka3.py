def print_params(a, b):
    return (a, b)

values_list = [1, 'строка']
param = print_params(*values_list)
print(param)