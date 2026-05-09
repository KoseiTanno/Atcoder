# 私の回答
# 正解
N,K = map(int,input().split())
A = list(map(int,input().split()))
now = A[0]
for i in range(1,N):
    now *= A[i]
    if len(str(now)) > K:
        now = 1
        continue
print(now)