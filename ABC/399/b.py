# 私の回答
# 正解
N = int(input())
P = list(map(int,input().split()))
r = 1
result = [0] * N
while(r < N+1):
    k = 0
    x = max(P)
    for i in range(N):
        if x == P[i]:
          result[i] = r
          k += 1
          P[i] = 0
    r += k
        
for i in range(N):
    print(result[i])