# 私の回答
# 正解
X = int(input())
N = int(input())
W = list(map(int,input().split()))
Q = int(input())
lst = []
weight = X
for i in range(Q):
    P = int(input())
    if P not in lst:
        weight += W[P-1]
        print(weight)
        lst.append(P)
    else:
        weight -= W[P-1]
        print(weight)
        lst.remove(P)