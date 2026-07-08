# 私の回答

import bisect
N = int(input())
L = sorted(list(map(int,input().split())))
cnt = 0
for i in range(N-1):
    for j in range(i+1,N-1):
        a,b = L[i],L[j]
        cnt += bisect.bisect_left(L,a+b) - (j+1)
print(cnt)