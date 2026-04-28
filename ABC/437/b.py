# 私の回答
# 正解
H,W,N = map(int,input().split())
grid = []
B = []
for i in range(H):
    grid.append(list(map(int,input().split())))
for i in range(N):
    B.append(int(input()))
cnt = [0] * N
for i in range(H):
    for j in range(W):
        if grid[i][j] in B:
            cnt[i] +=  1
print(max(cnt))