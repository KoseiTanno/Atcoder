# https://atcoder.jp/contests/abc365/tasks/abc365_a
# 私の回答
# 正解

Y = int(input())
ans = 365

if Y % 400 == 0:
    ans = 366

if Y % 4 == 0 and Y % 100 != 0:
    ans = 366

print(ans)