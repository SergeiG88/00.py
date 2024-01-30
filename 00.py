# import numpy as np
# import pygame as pg
#
#
# fps = pg.time.Clock()
# screen = pg.display.set_mode((510, 510))
# map_colors = np.arange(0, 510)
# for i in map_colors:
#     for j in map_colors:
#         surf = pg.Surface((1, 1))
#         surf.fill((i // 2, i // 2, i // 2))
#         screen.blit(surf, (i, j))
#
# r = 0
# g = 0
# b = 255
# circle_start_size = 1
# circle_end_size = 50
# current_size = circle_end_size
# size_dir = 1
#
# while True:
#
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             exit()
#     if pg.mouse.get_pressed()[0]:
#         pg.draw.circle(screen, (r, g, b), pg.mouse.get_pos(), current_size, 2)
#
#     if r < 255 and g == 0:
#         r += 1
#         b -= 1
#     elif g < 255 and b == 0:
#         g += 1
#         r -= 1
#     else:
#         b += 1
#         g -= 1
#
#     if current_size in (circle_start_size, circle_end_size):
#         size_dir *= -1
#
#     current_size += size_dir
#
#     fps.tick(60)
#     pg.display.update()


import datetime
import requests
from bs4 import BeautifulSoup as Bs
import csv


def write_cmc_top():
    url = "https://coinmarketcap.com/ru/"
    html = requests.get(url)
    soup = Bs(html.text, 'lxml')
    div = soup.find('div', class_="sc-14cb040a-2 hptPYH")
    table = div.find('tbody')
    tr = table.find_all('tr', style="cursor:pointer")[:10]
    all_types = []
    coast = []
    int_coast = []
    for p in tr:
        value = p.find('p', {'font-weight': 'semibold'}).text
        coin = p.find('span', {'data-nosnippet': 'true', 'class': 'sc-7bc56c81-1'}).text
        all_types.append(value)
        coast.append(coin[1:])
        int_coast.append(int(coin[1:].replace(',', '')))

    data_file_name = datetime.datetime.now().strftime("%H.%M. %d.%m.%Y") + '.csv'
    with open(data_file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(['Name', 'MC', 'MP'])
        count = 0
        for row in range(len(all_types)):
            writer.writerow([all_types[count], coast[count], f'{round(int_coast[count] / sum(int_coast) * 100)}%'])
            count += 1
    print(f"Данные успешно записаны в файл: {data_file_name}")


write_cmc_top()
