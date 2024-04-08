class House:
    numberOfFloors = 10

h1 = House()
for i in range(h1.numberOfFloors):
    h1.numberOfFloors += 1
    print('Текущий этаж равен', h1.numberOfFloors)
