import math


def solution(fuel, powers, distances):
    def get_time(fuel, power, distance):
        if fuel * power * fuel / 2 > distance:
            return math.sqrt(distance * 2 / power)
        return fuel + (distance - (fuel * power * fuel / 2)) / (power * fuel)

    a = []
    max_value, max_idx = -1, -1
    for idx in range(len(powers)):
        value = distances[idx] / powers[idx]
        if max_value < value:
            max_value = value
            max_idx = idx

    if fuel == len(powers):
        answer = get_time(1, powers[max_idx], distances[max_idx])
        return math.ceil(answer)

    start_fuel = fuel - len(powers) + 1
    rest_power_avg = (sum(powers) - powers[max_idx]) / (len(powers) - 1)
    rest_power_dist = sum(distances) - distances[max_idx]
    answer = 999999999999
    for f in range(start_fuel, 1, -2):
        rest_fuel = fuel - f
        time1 = get_time(f, powers[max_idx], distances[max_idx])
        time2 = get_time(rest_fuel, rest_power_avg, rest_power_dist)
        time = max(time1, time2)
        print(f, time1, time2)
        answer = min(answer, time)

    return math.ceil(answer)


sol = solution(19, [40, 30, 20, 10], [1000, 2000, 3000, 4000])
print(sol)
