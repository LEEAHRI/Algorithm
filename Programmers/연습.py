def solution(n):
    a = []
    for x in range(n):
        if n // x == 1:
            a.append(x)

    print(a)
