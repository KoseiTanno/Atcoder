# https://atcoder.jp/contests/abc384/tasks/abc384_a
# 私の回答
# 正解
A = list(input().split())
S = list(input())
res = []
for i in range(int(A[0])):
    if S[i] != A[1]:
        res.append(A[2])
    else:
        res.append(A[1])
print("".join(res))