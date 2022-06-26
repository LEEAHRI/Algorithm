from enum import Enum
from functools import cmp_to_key

data = [[1, 0, 11], [3, 1, 15], [2, 0, 16], [4, 0, 17], [2, 0, 15], [2, 1, 14], [2, 0, 12]]


class BlindDate:
    DAY_OF_THE_WEEK_PRIORITY = [DayOfTheWeekEnum.토, DayOfTheWeekEnum.금, DayOfTheWeekEnum.일, DayOfTheWeekEnum.수,
                                DayOfTheWeekEnum.목, DayOfTheWeekEnum.화, DayOfTheWeekEnum.월]
    def __init__(self):

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
        if BlindDate.DAY_OF_THE_WEEK_PRIORITY.index(day_of_the_week_a) > BlindDate.DAY_OF_THE_WEEK_PRIORITY.index(
                day_of_the_week_b):
            return 1
        return -1

    def Solution(date):
        blind_dates = [BlindDate(item[0], item[1], item[2], day_of_the_week) for day_of_the_week, item in
                       enumerate(data)]
        sorted_blind_dates = sorted(blind_dates, key=cmp_to_key(BlindDate.comparator))
        best_blind_dates, worst_blind_dates = sorted_blind_dates[0], sorted_blind_dates[-1]
        answer = [best_blind_dates.day_of_the_week.value,
                  worst_blind_dates.day_of_the_week.value if worst_blind_dates.is_not_recommended() else -1]
        return answer
