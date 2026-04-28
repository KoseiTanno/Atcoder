# 私の回答
# 正解
N = int(input())
grid = [[0] * N for _ in range(N)]
grid[0][(N-1)//2] = 1
r = 0
c = (N-1)//2
k = 1
for _ in range(N**2-1):
    if grid[(r-1)%N][(c+1)%N] == 0:
        grid[(r-1)%N][(c+1)%N] = k+1
        r = (r-1)%N
        c = (c+1)%N
    else:
        grid[(r+1)%N][c] = k+1
        r = (r+1)%N
    k += 1
for i in range(N):
    print(*grid[i])