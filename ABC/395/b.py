# 私の回答
# 正解
# 指定された模様を見て、その模様になるようのrange指定を考える
N = int(input())
grid = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(i,N-i):
            for l in range(i,N-j):
                if i <= j:
                    if i % 2 != 0:
                        grid[k][j] = "."
                    else:
                        grid[k][j] = "#"
for i in range(N):
    print("".join(grid[i]))