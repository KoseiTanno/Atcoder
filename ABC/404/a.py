# 私の回答
# 正解
S = input()
A = "abcdefghijklmnopqrstuvwxyz"
N = len(A)
for i in range(N):
    if A[i] not in S:
        print(A[i])
        exit()