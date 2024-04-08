class Vehicle:
    vehicle_type = 'none'

class Car:
    price = 1000000
    vehicle_type = 12

    def horse_powers(self):
        print('начальная цена', self.price)
        print('начальные силы', self.vehicle_type)

class Nissan(Vehicle, Car):
    price = 200
    vehicle_type = 5

    def horse_powers(self):
        print('цена машины', self.price)
        print('силы', self.vehicle_type)


print('Машина')
my_car = Car()
my_car.horse_powers()

print('Ниссан')
my_car = Nissan()
my_car.horse_powers()



