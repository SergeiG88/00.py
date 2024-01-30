class Buiding:

    def __init__(self):
        self.numberOfFloors = 5
        self.buildingType = 'other'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


dom = Buiding()
dom2 = Buiding()

print(f'2:{dom2.numberOfFloors, dom2.buildingType} 1:{dom.numberOfFloors, dom.buildingType}')
if dom == dom2:
    print('Yes')
else:
    print('No')
