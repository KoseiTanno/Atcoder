# https://atcoder.jp/contests/abc368/tasks/abc368_a
# 私の回答
# 正解

N,K = map(int,input().split())
A = list(input().split())
print(*(A[N-K:]+A[:N-K]))

