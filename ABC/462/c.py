# 私の回答
# 正解

N = int(input())
dots = []
for _ in range(N):
    x,y = map(int,input().split())
    dots.append([x,y])
dots.sort()
cnt = 0
min_y = 10**18

for x,y in dots:
    if y < min_y:
        cnt += 1
    min_y = min(min_y,y)
print(cnt)
