n, k = map(int, input().split())
a = list(map(int, input().split()))
# 중복 없는(제거하는) 자료구조
res = set()
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            # set은 append가 없다.
            res.add(a[i] + a[j] + a[m])
# sort 해주기 위해서 list화 시킨다.
res = list(res)
res.sort(reverse=True)
print(res[k - 1])
