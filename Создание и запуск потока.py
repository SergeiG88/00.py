import threading
import time


def take_turns(what):

    for i in what:
        with locker:
            print(i)


        time.sleep(1)
locker = threading.Lock()


t1 = threading.Thread(target=take_turns, args=(range(1,11),))
# t2 = threading.Thread(target=take_turns, args=('abcdefghij',))


t1.start()
# t2.start()
take_turns('abcdefghij')
t1.join()
# t2.join()
#
#
# #
# import random
# from threading import Thread
# import time
# from collections import defaultdict
#
# Warrior = (None,'аа')
#
#
# class Knight(Thread):
#
#     def __init__(self, name, skill, *args, **kwargs):
#         super(Knight, self).__init__(*args, **kwargs)
#         self.name = name
#         self.skill = skill
#         self.enemies = 100
#
#     def run(self):
#         # catch = defaultdict(int)
#         for i in range(self.skill):
#             for a in range(self.enemies):
#                 print(f'{self.name}, Сражается {i}  день(дня)..., Осталось {a} войнов', flush=True)
#                 # time.sleep(amount)
#         else:
#                 print(f'{self.name}', flush=True)
#             # warrior = random.choice(Warrior)
#         # time.sleep(5)
#         # catch -= 10
#         # print(f'Осталось рыцарей {self.name}')
#         # for a in catch.items():
#         #     print(f'Осталось воинов - {a}')
#
#         print(f'{self.name} одержал победу:')
#
#
#
# knight1 = Knight(name='Sir Lancelot', skill=10) # Низкий уровень умения
# knight2 = Knight(name='Sir Galahadir', skill=20)  # Высокий уровень умения
#
# knight1.start()
# knight2.start()
#
# knight1.join()
# knight2.join()
#
# print('Все битвы закончились!')
