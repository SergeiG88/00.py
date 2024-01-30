class Pet:
    legs = 4
    # has_tail = True


    def inspect(self):
        print('Всего ног', self.legs)
        # print('Хвост присутствует -', 'да' if self.has_tail else 'нет')

class Cat(Pet):

    def sound(self):
        print('мяу')

class Dog(Pet):

    def sound(self):
        print('гав')

# class Hanster(Pet):
#
#     def sound(self):
#         print('щщщ')

print('котик')
my_pet = Cat()
my_pet.inspect()
my_pet.sound()

# print('собачка')
# my_pet = Dog()
# my_pet.inspect()
# my_pet.sound()

# print('хомячок')
# my_pet = Hanster()
# my_pet.inspect()
# my_pet.sound()