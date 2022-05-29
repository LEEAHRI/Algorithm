from enum import Enum
from functools import cmp_to_key


class AirEnum(Enum):
    맑음 = 1
    구름조금 = 2
    구름많음 = 3
    흐림 = 4


class RainfallEnum(Enum):
    없음 = 0
    비 = 1
    눈 = 2


class DayOfTheWeekEnum(Enum):
    월 = 0
    화 = 1
    수 = 2
    목 = 3
    금 = 4
    토 = 5
    일 = 6


class Weather:
    def __init__(self, air_value, rainfall_value):
        self.air = AirEnum(air_value)
        self.rainfall = RainfallEnum(rainfall_value)

    def get_score(self):
        if self.rainfall == RainfallEnum.비:
            return 5
        if self.rainfall == RainfallEnum.눈:
            return 14
        if self.air == AirEnum.맑음 or self.air == AirEnum.구름조금:
            return 20
        if self.air == AirEnum.구름많음:
            return 17
        if self.air == AirEnum.흐림:
            return 10

    def is_not_recommended(self):
        return self.air == AirEnum.흐림 or self.rainfall == RainfallEnum.비


class Temperature:
    def __init__(self, value):
        self.value = value
        self.score = 20 - abs(22 - self.value)

    def get_score(self):
        return self.score

    def is_not_recommended(self):
        return self.value >= 30 or self.value <= 0


class BlindDate:
    DAY_OF_THE_WEEK_PRIORITY = [DayOfTheWeekEnum.토, DayOfTheWeekEnum.금, DayOfTheWeekEnum.일, DayOfTheWeekEnum.수,
                                DayOfTheWeekEnum.목, DayOfTheWeekEnum.화, DayOfTheWeekEnum.월]

    def __init__(self, air_value, rainfall_value, temperature_value, day_of_the_week):
        self.temperature = Temperature(temperature_value)
        self.weather = Weather(air_value, rainfall_value)
        self.day_of_the_week = DayOfTheWeekEnum(day_of_the_week)

    def get_score(self):
        temperature_score = self.temperature.get_score()
        weather_score = self.weather.get_score()
        return temperature_score + weather_score

    def is_not_recommended(self):
        return self.temperature.is_not_recommended() or self.weather.is_not_recommended()

    @staticmethod
    def comparator(blind_date_a, blind_date_b):
        a_score = blind_date_a.get_score()
        b_score = blind_date_b.get_score()
        if a_score != b_score:
            if a_score < b_score:
                return 1
            return -1

        day_of_the_week_a = blind_date_a.day_of_the_week
        day_of_the_week_b = blind_date_b.day_of_the_week
        if BlindDate.DAY_OF_THE_WEEK_PRIORITY.index(day_of_the_week_a) > \
                BlindDate.DAY_OF_THE_WEEK_PRIORITY.index(day_of_the_week_b):
            return 1
        return -1


def solution(data):
    blind_dates = [BlindDate(item[0], item[1], item[2], day_of_the_week) for day_of_the_week, item in enumerate(data)]
    sorted_blind_dates = sorted(blind_dates, key=cmp_to_key(BlindDate.comparator))
    best_blind_dates, worst_blind_dates = sorted_blind_dates[0], sorted_blind_dates[-1]
    answer = [best_blind_dates.day_of_the_week.value,
              worst_blind_dates.day_of_the_week.value if worst_blind_dates.is_not_recommended() else -1]
    return answer
