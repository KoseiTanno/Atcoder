H,W = map(int,input().split())
grid = [input() for _ in range(H)]

rows = [i for i in range(H) if "#" in grid[i]]
cols = [j for j in range(W) if any(grid[i][j] == "#" for i in range(H))]

for i in range(rows[0],rows[-1]+1):
    print(grid[i][cols[0]:cols[-1]+1])