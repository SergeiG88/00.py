# # Задание:
# # Моделирование программы для управления данными о движении товаров на складе и эффективной обработки запросов на
# # обновление информации в многопользовательской среде.
# #
# # Представим, что у вас есть система управления складом, где каждую минуту поступают запросы на обновление информации о
# # поступлении товаров и отгрузке товаров.
# # Наша задача заключается в разработке программы, которая будет эффективно обрабатывать эти запросы в
# # многопользовательской среде, с использованием механизма мультипроцессорности для обеспечения быстрой реакции на
# # поступающие данные.
# #
# # Создайте класс WarehouseManager - менеджера склада, который будет обладать следующими свойствами:
# # Атрибут data - словарь, где ключ - название продукта, а значение - его кол-во. (изначально пустой)
# # Метод process_request - реализует запрос (действие с товаром), принимая request - кортеж.
# # Есть 2 действия: receipt - получение, shipment - отгрузка.
# # а) В случае получения данные должны поступить в data (добавить пару, если её не было и изменить значение ключа, если
# # позиция уже была в словаре)
# # б) В случае отгрузки данные товара должны уменьшаться (если товар есть в data и если товара больше чем 0).
# #
# # 3.Метод run - принимает запросы и создаёт для каждого свой параллельный процесс, запускает его(start) и замораживает
# # (join).
# #
# #
# # Пример работы:
# # # Создаем менеджера склада
# # manager = WarehouseManager()
# #
# # # Множество запросов на изменение данных о складских запасах
# # requests = [
# #     ("product1", "receipt", 100),
# #     ("product2", "receipt", 150),
# #     ("product1", "shipment", 30),
# #     ("product3", "receipt", 200),
# #     ("product2", "shipment", 50)
# # ]
# #
# # # Запускаем обработку запросов
# # manager.run(requests)
# #
# # # Выводим обновленные данные о складских запасах
# # print(manager.data)
# #
# # Вывод на консоль:
# # {"product1": 70, "product2": 100, "product3": 200}
#
#
# import multiprocessing
# from multiprocessing import Process
#
#
# class WarehouseManager(Process):
#     data = {}
#
#     # def __init__(self):
#     #     self.data = {}
#     # {"product1": 70, "product2": 100, "product3": 200}
#
#     def process_request(self, request):
#         product, action, quantity = request
#
#         if action == "receipt":
#             if product in self.data:
#                 self.data[product] += quantity
#             else:
#                 self.data[product] = quantity
#         elif action == "shipment":
#             if product in self.data and self.data[product] > 0:
#                 self.data[product] -= quantity
#
#         # print(f'{self.data=}')
#
#     def run(self, requests):
#         # self.data = {"product1": 70, "product2": 100, "product3": 200}
#
#         processes = []
#         for request in requests:
#             # print(request)
#
#             # for key in self.data:
#             #     print(f'{key}')
#             # {"product1": 70, "product2": 100, "product3": 200}
#
#             # print(f'{self.data}')
#             p = multiprocessing.Process(target=self.process_request, args=(request,))
#             processes.append(p)
#
#         for p in processes:
#             p.start()
#
#         for p in processes:
#             p.join()
#
#
# manager = WarehouseManager()
#
# requests = [
#     ("product1", "receipt", 100),
#     ("product2", "receipt", 150),
#     ("product1", "shipment", 30),
#     ("product3", "receipt", 200),
#     ("product2", "shipment", 50)
# ]
#
# if __name__ == '__main__':
#     manager.run(requests)
# #
# print(manager.data)

from datetime import datetime

class SuperDate(datetime):
    list_season = {(12, 1, 2): 'Winter', range(3, 4, 5): 'Autumn', range(6, 7, 8): 'Summer', range(9, 10, 11): 'Spring'}
    dict_time = {range(6, 12): 'Morning', range(12, 18): 'Day', range(18, 0): 'Evening', range(0, 6): 'Night'}

    def __init__(self, year, month, day, hour):
        self.date = datetime(year, month, day, hour)

    def get_season(self):
        for current in self.list_season:
            if self.month in current:
                return self.list_season[current]


    def get_time_of_day(self):
        for current in self.dict_time:
            if self.hour in current:
                return self.dict_time[current]

if __name__ == '__main__':


    a = SuperDate( 2024, 2, 22, 12)
    print(a.get_season())
    print(a.get_time_of_day())


































