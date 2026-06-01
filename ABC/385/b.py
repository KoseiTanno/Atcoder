# 私の回答
# 不正解
H,W,X,Y = map(int,input().split())
S = [[input()] for i in range(H)]
T = list(input())
N = len(T)
C = 0
for x in range(N):
    for i in range(X,H):
        for j in range(Y,W):
            if S[i][j] == "@":
                C += 1
            if T[x] == "U" and S[i-1][j] != "#":
                X = i-1
            elif T[x] == "D" and S[i+1][j] != "#":
                X = i+1
            elif T[x] == "L" and S[i][j-1] != "#":
                Y = j-1
            elif T[x] == "R" and S[i][j+1] != "#":
                Y = j+1
print(X,Y)
print(C)