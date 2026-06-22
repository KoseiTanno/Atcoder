# https://atcoder.jp/contests/abc370/tasks/abc370_a
# 私の回答
# 正解

L,R = map(int,input().split())
if L == R:
    print("Invalid")
elif L == 1:
    print("Yes")
else:
    print("No")
