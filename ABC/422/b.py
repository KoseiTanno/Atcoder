# 私の回答
# 正解
# だが、1時間ぐらいかけてしまった
# H,W = map(int,input().split())
# grid = ["."*(W+2)]
# ok = False
# black = False
# for i in range(1,H+1):
#     grid.append(input())
#     grid[i] = "." + grid[i] + "."
# grid.append("."*(W*2))
# for k in range(1,H+1):
#     for l in range(1,W+1):
#         if grid[k][l] == "#":
#             cnt = 0
#             black = True
#             if grid[k-1][l] == "#":
#                 cnt += 1
#             if grid[k][l-1] == "#":
#                 cnt += 1
#             if grid[k][l+1] == "#":
#                 cnt += 1
#             if grid[k+1][l] == "#":
#                 cnt += 1
#             if cnt != 2 and cnt != 4:
#                 print("No")
#                 exit()
#             if cnt == 2 | cnt == 4:
#                 ok = True
#                 continue                
#             if cnt != 2 and cnt != 4 and ok == False and black == True:
#                 print("No")
#                 exit()
# print("Yes")

# 模範回答
# TrueやFalseは内部で1、0として扱われるので、真偽を確かめてcntに足したり引いたりするときは真偽をそのまま加減できる
# あるマスの隣あうマスをインデックスで指定するためのリストを作ると便利
# exit()の中に処理を入れると、その処理をしてからexitする
H, W = map(int, input().split())
S = [input() for i in range(H)]

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(H):
    for j in range(W):
        cnt = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < H and 0 <= nj < W:
                cnt += (S[ni][nj] == '#')
        if S[i][j] == '#' and cnt != 2 and cnt != 4:
            exit(print("No"))
print("Yes")