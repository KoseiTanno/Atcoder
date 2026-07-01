# https://atcoder.jp/contests/abc365/tasks/abc365_b
# 私の回答
# 正解

N = int(input())
A = list(map(int,input().split()))
A[A.index(max(A))] = 0
print(A.index(max(A))+1)

