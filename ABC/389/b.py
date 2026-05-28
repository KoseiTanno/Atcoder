# 私の回答
# 正解
X = int(input())

def kaijou(num):
    res = num
    for i in range(num-1,1,-1):
        res *= i
    return res

for i in range(1,30):
    if kaijou(i) == X:
        print(i)
        exit()
