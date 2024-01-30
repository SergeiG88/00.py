from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super().__init__()
        self.name = name
        self.skill = skill
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!', flush=True)
        while self.enemies > 0:
            self.enemies -= self.skill
            self.days += 1
            print(f'{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.', flush=True)
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {self.days} дней!', flush=True)

knight1 = Knight(name='Sir Lancelot', skill=10)
knight2 = Knight(name='Sir Galahad', skill=20)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print('Все битвы закончились!')