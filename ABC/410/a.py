# 私の回答
# 正解
N = int(input())
A = list(map(int,input().split()))
K = int(input())
cnt = 0
for i in range(N):
    if A[i] >= K:
        cnt += 1
print(cnt)