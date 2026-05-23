# 私の回答
# 正解
X = list(input())
N = len(X)
cnt = 0
for i in range(1,N):
    if X[i] == X[i-1]:
        cnt += 1

if (N + cnt) % 2 != 0:
    print(cnt + 1)
elif X[0] == "o":
    print(cnt + 2)
else:
    print(cnt)