# https://atcoder.jp/contests/abc367/tasks/abc367_a
# 私の回答
# 正解
A,sleep,wake = map(int,input().split())
if sleep > wake:
    wake += 24
if sleep < A < wake or sleep < A+24 < wake:
    print("No")
else:
    print("Yes")