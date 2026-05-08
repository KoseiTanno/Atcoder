# 私の回答
# 正解
A,B = map(int,input().split())
C = A//B
D = (A//B) + 1
E = A/B
if abs(E-C) - abs(E-D) > 0:
    print(D)
    exit()
else:
    print(C)