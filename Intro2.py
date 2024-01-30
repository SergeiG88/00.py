from pprint import pprint

# file_name = 'byron.txt'
# file = open(file_name, mode='rb')  # mode (режим): чтение бинарное
# file_content = file.read()
# file.close()
# pprint(file.content)

# file_name = 'pushkin.txt'
# file = open(file_name, mode='rb')  # mode (режим): чтение бинарное
# file_content = file.read()
# file.close()
# pprint(file_content.decode('utf8'))

file_name = 'repka_1.txt'
file = open(file_name, mode='r', encoding='utf8')  # mode (режим): чтение бинарное
file_content = file.read()
file.close()
pprint(file_content)