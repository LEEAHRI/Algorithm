T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 슬라이싱 s번째부터 e번째 까지
    a = a[s - 1:e]
    a.sort()
    print("#%d %d" % (t+1, a[k - 1]))

