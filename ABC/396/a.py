# 私の回答
# 正解
N = int(input())
A = list(map(int,input().split()))
pre = A[0]
cnt = 1
i = 1
while (cnt < 3) and (i < N):
    if A[i-1] == A[i]:
        cnt += 1
    else:
        cnt = 1
    i += 1
print("Yes" if cnt >= 3 else "No")