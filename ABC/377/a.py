# https://atcoder.jp/contests/abc377/tasks/abc377_a
# 私の回答
# 正解

S = list(input())
A = S.count("A")
B = S.count("B")
C = S.count("C")
if A and B and C:
    print("Yes")
else:
    print("No")