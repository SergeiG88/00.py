# import os
# Для Windows
# path = 'C:\\Windows\\help'
#
# # Пройтись по всем файлам директории
# count = 0
# for dirpath, dirnames, filenames in os.walk(path):
#     print(dirpath, dirnames, filenames)
#     count += len(filenames)
#
# print(count)


# import os
#
# path = 'C:/Windows/help'
# path_normalized = os.path.normpath(path)
# print(path_normalized)
#
# # # Пройтись по всем файлам директории
# count = 0
# for dirpath, dirnames, filenames in os.walk(path):
#     print(dirpath, dirnames, filenames)
#     count += len(filenames)
#
# print(count)

## Время создания файла

# import os
#
# path = 'C:/Windows/help'
# path_normalized = os.path.normpath(path)
# print(path_normalized)
#
# # # Пройтись по всем файлам директории
# count = 0
# for dirpath, dirnames, filenames in os.walk(path):
#     print(dirpath, dirnames, filenames)
#     count += len(filenames)
#     for file in filenames:
#         full_name_path = dirpath + '\\' + file
#         print(full_name_path, os.path.getatime(full_name_path))
#
# print(count)


import time

import os

# path = 'C:/Windows/help'
# path_normalized = os.path.normpath(path)
# print(path_normalized)
#
# # # Пройтись по всем файлам директории
# count = 0
# for dirpath, dirnames, filenames in os.walk(path):
#     print(dirpath, dirnames, filenames)
#     count += len(filenames)
#     for file in filenames:
#         full_name_path = dirpath + '\\' + file#
#         secs = os.path.getatime(full_name_path)
#         file_time = time.gmtime(secs)
#         if file_time [0] == 2023:
#             print(full_name_path, secs)
#
# print(count)


# path = 'C:/Windows/help'
# path_normalized = os.path.normpath(path)
# print(path_normalized)
#
# # # Пройтись по всем файлам директории
# count = 0
# for dirpath, dirnames, filenames in os.walk(path):
#     print(dirpath, dirnames, filenames)
#     count += len(filenames)
#     for file in filenames:
#         full_name_path = os.path.join(dirpath, file)
#         secs = os.path.getatime(full_name_path)
#         file_time = time.gmtime(secs)
#         if file_time [0] == 2023:
#             print(full_name_path, secs)
#
# print(count)


# path = 'C:/Windows/help'
# path_normalized = os.path.normpath(path)
# print(path_normalized)
#
# # # Пройтись по всем файлам директории
# count = 0
# for dirpath, dirnames, filenames in os.walk(path):
#     print('*' * 27)
#     print(dirpath, dirnames, filenames)
#     print(os.path.dirname(dirpath))
#     count += len(filenames)
#     for file in filenames:
#         full_name_path = os.path.join(dirpath, file)
#         secs = os.path.getatime(full_name_path)
#         file_time = time.gmtime(secs)
#         if file_time [0] == 2023:
#             print(full_name_path, secs)
#
# print(count)


path = 'C:/Windows/help'
path_normalized = os.path.normpath(path)
print(path_normalized)

# # Пройтись по всем файлам директории
count = 0
for dirpath, dirnames, filenames in os.walk(path):
    print('*' * 27)
    print(dirpath, dirnames, filenames)
    print(os.path.dirname(dirpath))
    count += len(filenames)
    for file in filenames:
        full_name_path = os.path.join(dirpath, file)
        secs = os.path.getatime(full_name_path)
        file_time = time.gmtime(secs)
        if file_time [0] == 2023:
            print(full_name_path, secs)

print(count)

print(__file__, os.path.dirname(__file__))