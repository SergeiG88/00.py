from datetime import datetime


class SuperDate(datetime):
    list_season = {(12, 1, 2): 'Winter', range(3, 4, 5): 'Spring', range(6, 7, 8): 'Summer', range(9, 10, 11): 'Autumn'}
    dict_time = {range(6, 12): 'Morning', range(12, 18): 'Day', range(18, 0): 'Evening', range(0, 6): 'Night'}

    def __init__(self, year, month, day, hour):
        self.date = datetime(year, month, day, hour)


    def get_season(self):
        for current in self.list_season:
            if self.date.month in current:
                return self.list_season[current]

    def get_time_of_day(self):
        for current in self.dict_time:
            if self.date.hour in current:
                return self.dict_time[current]


if __name__ == '__main__':

    a = SuperDate(2024, 2, 22, 12)

    print(a.get_season())
    print(a.get_time_of_day())
