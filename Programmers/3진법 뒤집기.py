## 10진법을 -> n진법으로 변환하는 함수
def solution(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


print(solution(45, 3))
