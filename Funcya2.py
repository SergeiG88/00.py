def print_them_all_v2(**kwargs):
    print('print_them_all_v2')
    print('тип kwargs', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент', key, '=', value)

print_them_all_v2(name='Вася', address='Moscow', home=42)