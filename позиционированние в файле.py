# from pprint import pprint
#
# file_name = 'tutu.txt'
# file = open(file_name, mode='r', encoding='utf8')
# # file_content = file.read()
# # file.close()
# print(file.tell())
#
# print('читаем 100 символов')
# file_content = file.read(100)
# print(file_content)
# print(file.tell())
#
# print('читаем остальное')
# file_content = file.read()
# print(file_content)
# print(file.tell())
#
# file.close()


# from pprint import pprint
#
# file_name = 'tutu.txt'
# file = open(file_name, mode='r', encoding='utf8')
#
# pprint(file.name)
# pprint(file.mode)
# pprint(file.encoding)
# pprint(file.closed)
#
# pprint(file.readable())
# pprint(file.writable())
# pprint(file.seekable())
#
# pprint(file.flush())

from pprint import pprint

file_name = 'tutu.txt'
file = open(file_name, mode='rb')
file_content = file.read()
file.close()
pprint(file_content)