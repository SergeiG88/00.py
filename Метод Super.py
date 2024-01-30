class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format( self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')

class VacuumCleaningRobot(Robot):

    def __init__(self, model):
        super().__init__(model=model)
        self.dust_bug = 0

    def operate(self):
        print('робот пылесосит пол, заполненность мешка для пыли', self.dust_bug)

roomba = VacuumCleaningRobot(model='roomba M505')
print(roomba)
roomba.operate()