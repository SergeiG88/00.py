import csv
import json

csv_filename = 'example.csv'
csv_data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Алексей', 47, 'Калуга']
]
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
print('CSV DATA:')
with open(csv_filename, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

json_filename = 'data.json'
json_data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
 }
with open(json_filename, 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)
print('\nJSON DATA:')
with open(json_filename, 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)