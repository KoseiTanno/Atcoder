# 私の回答
# 正解
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = [i for i in range(1,M+1)]
flag = True
for i in range(N+1):
    for j in range(M):
        if B[j] not in A:
            flag = False
    if not flag:
        print(i)
        exit()
    else:
        del A[-1]