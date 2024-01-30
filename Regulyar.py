# import re
#
# def extract_image_links(html_text):
#     image_links = re.findall(r'(https?://\S+\.(?:jpg|jpeg|png|gif))', html_text)
#     return image_links
#
#
# html_text = """
# <html>
# <head>
#     <title>Test Page</title>
# </head>
# <body>
#     <img src="https://example.com/image1.jpg">
#     <img src="https://example.com/image2.jpeg">
#     <img src="https://example.com/image3.png">
#     <img src="https://example.com/image4.gif">
#
# </body>
# </html>
# """
#
# image_links = extract_image_links(html_text)
# print(image_links)
#


import csv


def write_holiday_cities(first_letter):
    cities_visited = set()
    cities_to_visit = set()
    cities_never_visited = set()

    with open('travel_notes.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name, visited, to_visit = row[0].split(',')
            if name.startswith(first_letter):
                cities_visited.update(visited.split(';'))
                cities_to_visit.update(to_visit.split(','))

    cities_never_visited = cities_to_visit.difference(cities_visited)

    next_city = sorted(cities_to_visit)[0]

    with open('holiday.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Посетили:"] + sorted(cities_visited))
        writer.writerow(["Хотят посетить:"] + sorted(cities_to_visit))
        writer.writerow(["Никогда не были в:"] + sorted(cities_never_visited))
        writer.writerow(["Следующим городом будет:"] + [next_city])


# Пример вызова функции для первой буквы "L"
write_holiday_cities('L')

#
# Этот код считывает данные из файла `travel_notes.csv`, находит информацию о городах для студентов с именами,
# начинающимися на заданную букву, а затем записывает информацию в файл `holiday.csv` в соответствии с требованиями задачи.
#
# Пожалуйста, замените символы в файле `travel_notes.csv` на фактические данные перед тем как запустить код.
#
# Если у вас возникнут дополнительные вопросы или пожелания, не стесняйтесь обращаться!