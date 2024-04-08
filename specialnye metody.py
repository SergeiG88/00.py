
class Car:
    price = 1000000
    powers = 12

    def horse_powers(self):
        print('лошадиных сил', self.powers)



class Nissan(Car):
    price = 2000
    powers = 15




# class Kia(Car):
#     price = 5000
#     powers = 88


print('Ниссан')
my_car = Nissan()
my_car.horse_powers()


# print('Киа')
# my_car = Kia()
# my_car.horse_powers()