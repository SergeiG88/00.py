def print_params(a=1, b='строка', c=True):
    return (a, b, c)
some_list = [1, 'строка', True]
param = print_params(*some_list)
print_params(b=25)
print_params(c=[1,2,3])
print(param)

