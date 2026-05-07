# 私の回答
# 正解
N = int(input())
D = list(map(int,input().split()))
for i in range(N-1):
    lst = []
    for j in range(i,N-1):
        lst.append(sum(D[i:j+1]))
    print(*lst)