# 二分探索で出ていく時間がクエリのタイム以下な
import bisect
N = int(input())
H_L = [list(map(int,input().split())) for _ in range(N)]
H_L = sorted(H_L,key=lambda x:x[1])
L_lst = [x[1] for x in H_L]
suffix_max = [0] * (N+1)
for i in range(N-1,-1,-1):
    suffix_max[i] = max(suffix_max[i+1],H_L[i][0])

Q = int(input())
T = list(map(int,input().split()))

for i in T:
    j = bisect.bisect_right(L_lst,i)
    print(suffix_max[j])