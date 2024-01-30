class Pets:
    legs = 4
    has_tail = True

    def __init__(self, name):
        self.name = name


    def inspect(self):
        print(self.__class__.__name__, self.name)
        print('всего ног', self.legs)
        print('хвост есть -', 'да' if self.has_tail else 'нет')
        print(self.__dict__)

pet = Pets(name='Кузя')
pet.legs = 5
pet.has_tail = False
pet.inspect()
print(pet.__class__ is Pets)
