def print_them_all_v3(*args, **kwargs):
    print('print_them_all_v3')
    print('тип args', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр', i, arg)
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент', key, '=', value)

#print_them_all_v3('Вася', 'Moskow', 25)
print_them_all_v3('Вася', 'Moscow', 25, name='Петя', address='Paris')