# 私の回答
# 正解

N,K = map(int,input().split())
A = sorted(list(map(int,input().split())))

def f(x):
    total = 0
    for i in A:
        total += (i+x-1)//x - 1
    return total

ok = 10**9+1
ng = 0
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    if f(mid) <= K:
        ok = mid
    else:
        ng = mid
print(ok)

