# n을 나누었을 때 나머지가 leetcode 이 되게 되는 가장작은 자연수 구하기
def solution(n):
    a = []
    for x in range(1,n):
        if n % x == 1:
            a.append(x)
    return min(a)
