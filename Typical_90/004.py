# 私の回答
# 正解
# 列と行の合計のリストを作って、それらを足して、重なった部分を引く
H,W = map(int,input().split())
A = [[*map(int,input().split())] for _ in range(H)]
row = []
line = []
ans = [[0] * W for _ in range(H)]
for i in range(H):
    row.append(sum(A[i]))
for i in range(W):
    cnt = 0
    for j in range(H):
        cnt += A[j][i]
    line.append(cnt)
for i in range(H):
    for j in range(W):
      ans[i][j] += row[i] + line[j] - A[i][j]
    print(*ans[i])