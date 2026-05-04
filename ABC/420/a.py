# 私の回答
# 正解
X,Y = map(int,input().split())
result = X+Y
if result > 12:
    print(result-12)
    exit()
print(result)