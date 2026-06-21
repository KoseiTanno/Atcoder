# https://atcoder.jp/contests/abc373/tasks/abc373_a
# 私の回答
# 正解

cnt = 0
for i in range(12):
    S = input()
    if len(S) == i+1:
        cnt += 1
print(cnt)