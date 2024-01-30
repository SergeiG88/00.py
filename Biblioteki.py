import multiprocessing


class WarehouseManager:
    def __init__(self):
        self.data = {}






    def process_request(self, request):
        product, action, quantity = request
        if action == "receipt":
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
        elif action == "shipment":
            if product in self.data and self.data[product] > 0:
                self.data[product] -= quantity

    def run(self, requests):
        processes = []

        for request in requests:
            q = multiprocessing.Process(target=self.process_request, args=(request,))
            processes.append(q)

        for q in processes:
            q.start()

        for q in processes:
            q.join()


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
