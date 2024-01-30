# a = 'team1_num'
# # # b = 5
# # print('В команде Мастера %s кода участников: %s!'%( a, b))
# print('В команде Мастера "%s" кода участников: 5!'%(a))

# a = 'team1_num'
# b = 'team2_num'
# print('Итого сегодня в команде %s 5 участников, а в команде %s 6 участников!'%( a, b))

# a = 'score_2'
# print('Команда {0} Волшебники данных решила задач: 42!'.format(a, 42))
# print('Команда {0} Волшебники данных решила задач: 42!'.format(a))

# team1_num = 5
# print('В команде Мастера кода участников: %s !'%(team1_num))
#
# team1_num = 5
# team2_num = 6
# print('Итого сегодня в командах участников: %s и %s !'%(team1_num, team2_num))
#
# score_2 = 42
# print('Команда Волшебники данных решила задач: {0} !'.format(score_2))
#
# team1_time = 18015.2
# print('Волшебники данных решили задачи за {0} c !'.format(team1_time))
#
# score_1 = 40
# score_2 = 42
# print(f'Команды решили {score_1} и {score_2} задачи')
#
# challenge_result =  "Результат битвы: победа команды Мастера кода!"
# print(f'{challenge_result}')
#
# tasks_total = 82
# time_avg = 350.4
# print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

import os
for root, dirs, files in os.walk(r'C:'):
    for name in files:
        fullname = os.path.join(root, name)
        print(fullname)
        if('pass' in fullname):
            print('Бинго!!!')