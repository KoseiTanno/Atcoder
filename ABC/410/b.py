# 私の回答
# 正解
N,Q = map(int,input().split())
X = list(map(int,input().split()))
cnt = [0] * N
result = []
for i in range(Q):
    if X[i] >= 1:
        result.append(X[i])
        cnt[X[i]-1] += 1
    elif X[i] == 0:
        for j in range(N):
            if cnt[j] == min(cnt):
                result.append(j+1)
                cnt[j] += 1
                break
print(*result)