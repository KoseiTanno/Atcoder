# 私の回答
# 正解
import bisect

N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))
cnt = 0

for i in range(N):
    # B[i]未満の個数
    a_ok = bisect.bisect_left(A,B[i])
    # B[i]超過の個数
    c_ok = N - bisect.bisect_right(C,B[i])
    cnt += a_ok*c_ok
print(cnt)
    