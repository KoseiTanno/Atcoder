# 私の回答
# 正解
N,S = map(int,input().split())
T = list(map(int,input().split()))
T.insert(0,0)
for i in range(1,N+1):
    if T[i] - T[i-1] >= S+1:
        print("No")
        exit()
print("Yes")