# 私の回答
# 正解
X,Y,Z = map(int,input().split())
for i in range(1000):
    if (X+i) / (Y+i) == Z:
        print("Yes")
        exit()
print("No")