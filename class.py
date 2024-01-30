# class House:
#     numberOfFloors = 10
#
# h1 = House()
# for i in range(h1.numberOfFloors):
#     h1.numberOfFloors += 1
#     print('Текущий этаж равен', h1.numberOfFloors)



import multiprocessing


class WarehouseManager:


    def __init__(self):
        self.data = {}


    def process_request(self, request):
        product, action, quantity = request
        if action == "receipt":
            if product in self.data:
                self.data[product] += quantity

# else:
# self.data[product] = quantity

        elif action == "shipment":
            if product in self.data and self.data[product] >= quantity:
                    self.data[product] -= quantity

            # print("Товара '{}' нет на складе". format(product))

    def run(self, requests):
        processes = []

        for request in requests:
            p = multiprocessing.Process(target=self.process_request, args=(request,))
        processes.append(p)
        p.start()

        for p in processes:
            p.join()
        print(f'Товары {requests}')
        # for p in processes:
        #     p.join()
# if __name__ == '__main__':
# Пример использования
manager = WarehouseManager()
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]
if __name__ == '__main__':
    manager.run(requests)
print(manager.data)
# if __name__ == '__main__':


# Шаги решения:
# 1. Определяем класс WarehouseManager с атрибутом data, который хранит данные о продуктах на складе.
# 2. Создаем метод process_request для обработки запросов в зависимости от действия (receipt - получение, shipment - отгрузка).
# 3. Метод process_request проверяет действие и обновляет данные о продукте в словаре data соответственно.
# 4. Определяем метод run, который создает отдельный процесс для каждого запроса, запускает их и ждет их завершения.
# 5. Создаем экземпляр класса WarehouseManager - manager.
# 6. Формируем запросы в формате кортежей и помещаем их в список requests.
# 7. Вызываем метод run у manager и передаем ему список запросов.
# 8. Выводим обновленные данные о продуктах на складе после обработки запросов.