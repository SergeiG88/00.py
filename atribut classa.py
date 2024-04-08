from random import randint


class Buiding:
    total = 0

    def __init__(self):
        Buiding.total += 1

family = []
family_size = 40
while len(family) < family_size:
    new_Building = Buiding()
    family.append(new_Building )

print(Buiding.total)
