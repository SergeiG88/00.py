
class Buiding:

    def __init__(self):
        self.numberOfFloors = 2
        self.buildingType = 'floor'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

b1 = Buiding
b2 = Buiding

if b1 == b2:

    print('Мы похожи', b1 == b2)


