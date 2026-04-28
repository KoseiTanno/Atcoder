# 私の回答
# 正解
N = int(input())
A = list(map(int,input().split()))
result = [-1] * N
for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            result[i] = j+1
print(*result)
