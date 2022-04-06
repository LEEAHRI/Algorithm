n = int(input())
a = list(map(int, input().split()))
#첫째자리까지 반올림
avg = round(sum(a)/n)
for idx, x in enumerate(a):

