# 私の回答
# 正解
H,W = map(int,input().split())
lst_x =[0,0,-1,1]
lst_y =[-1,1,0,0]
result = []
for i in range(H):
    lst = [0] * W
    for j in range(W):
        for k in range(4):
            x = i - lst_x[k]
            y = j - lst_y[k]
            if (0 <= x <= H-1) and (0 <= y <= W-1):
                lst[j] += 1
    result.append(lst)
for i in range(H):
    print(*result[i])