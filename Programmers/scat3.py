def solution(C, F, X):
    def get_time(n):
        sum = X / (2.0 + F * (n - 1))
        for i in range(0, n - 1):
            sum += C / (2.0 + F * i)
        return sum

    time = round(X / 2.0, 6)
    if C < X:
        for n in range(1, 50):
            time = min(time, get_time(n))

    return round(time, 6)