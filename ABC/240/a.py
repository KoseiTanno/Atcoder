# https://atcoder.jp/contests/abc240/tasks/abc240_a
# 私の回答
# 正解

a,b = map(int,input().split())

if abs(b-a) == 1:
    print("Yes")
elif a == 1 and b == 10:
    print("Yes")
else:
    print("No")