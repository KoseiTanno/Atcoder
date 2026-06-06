# https://atcoder.jp/contests/abc383/tasks/abc383_a
# 私の回答
# 正解

N = int(input())
grid = [list(map(int,input().split())) for i in range(N)]
water = 0
pre = 0
for i in range(N):
    water -= grid[i][0] - pre
    if water < 0:
        water = 0
    water += grid[i][1]
    pre = grid[i][0]
print(water)
