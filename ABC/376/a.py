# https://atcoder.jp/contests/abc376/tasks/abc376_a
# 私の回答
# 正解

N,C = map(int,input().split())
T = list(map(int,input().split()))
cnt = 1
pre = T[0]
for i in range(1,N):
    if T[i] - pre >= C:
        cnt += 1
        pre = T[i]
print(cnt)