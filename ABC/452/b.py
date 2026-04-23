# 私の回答
# 正解
# print関数のendという第二引数を覚えた　
H,W = map(int,input().split())
for i in range(H):
    for j in range(W):
        if j == W-1:
            print("#")
        elif i == 0 or i == H-1 or j == 0:
            print("#",end="")
        else:
            print(".",end="")