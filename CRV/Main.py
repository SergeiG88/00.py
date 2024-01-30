import csv

name = []
have_visit = set()
want_to_visit = set()


def write_holiday_cities(first_letter):
    with open(file='travel-notes.csv', mode='r', newline='', encoding='utf-8') as data_file:
        read_file = csv.reader(data_file, delimiter=',')
        for read_line in read_file:
            if first_letter in read_line[0][0]:
                for row in read_line[0].split(':'):
                    name.append(row)
                for row in read_line[1].split(':'):
                    have_visit.add(row)
                for row in read_line[2].split(':'):
                    want_to_visit.add(row)

    with open(file='holiday.csv', mode='w', newline='', encoding='utf-8') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(('Были в городах: ', sorted(have_visit)))
        writer.writerow(('Хотят посетить города: ', sorted(want_to_visit)))
        writer.writerow(('Не были в городах: ', sorted(want_to_visit.difference(have_visit))))
        writer.writerow(('Первый город для посещения: ', sorted(want_to_visit.difference(have_visit))[0]))

write_holiday_cities(first_letter='L')
