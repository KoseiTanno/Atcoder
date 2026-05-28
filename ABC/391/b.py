# わたしの回答
# 正解
# grid_tの一番最初の要素と合っているところを見つけたら調査開始
N,M = map(int,input().split())
grid_s = [list(input()) for i in range(N)]
grid_t = [list(input()) for i in range(M)]
for i in range(N-M+1):
    for j in range(N-M+1):
        if grid_s[i][j] == grid_t[0][0]:
            cnt = 0
            for k in range(M):
                for l in range(M):
                    if grid_s[i+k][j+l] == grid_t[k][l]:
                        cnt += 1
                    else:
                        break
            if cnt == M**2:
                print(i+1,j+1)

