# https://atcoder.jp/contests/abc366/tasks/abc366_a
# 私の回答
# 正解

N,T,A = map(int,input().split())
if (N-T-A) < abs(T-A):
    print("Yes")
else:
    print("No")