from pprint import pprint

file_name = 'tutu.txt'
file = open(file_name, mode='rb')
file_content = file.read()
file.close()
pprint(file_content)


# file_name = 'repka_1.txt'
# file = open(file_name, mode='rb')  # mode (режим): чтение бинарное
# file_content = file.read()
# file.close()
# pprint(file_content.decode('utf8'))

# file_name = 'repka_1.txt'
# file = open(file_name, mode='r', encoding='utf8')
# file_content = file.read()
# file.close()
# pprint(file_content)