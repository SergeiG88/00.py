
file_name = 'tutu.txt'
file = open(file_name, mode='r', encoding='utf8')
for line in file: # если файл огромный - будет читать только строку
    print(line, end='')
file.close()


file_name = 'repka_1.txt'
file = open(file_name, mode='r', encoding='utf8')
lines = file.readlines
for line in lines(): # если файл огромный - будет читать только строку
    print(line)
file.close()

file_name = 'repka_1.txt'
file = open(file_name, mode='r', encoding='utf8')
line = True
for line in file:
# while line:
#     line = file.readline()
    if 'дуб' in line:
        print('Дуб найден в строке', line)
        break
else:
    print('Тут дуба нет')
file.close()

file_name = 'repka_1.txt'
with open(file_name, mode='r', encoding='utf8') as line:
    for file in line:
        print(file)
# print(file.closed)