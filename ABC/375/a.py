# https://atcoder.jp/contests/abc375/tasks/abc375_a
# 私の回答
# 正解

N = int(input())
S = input()
cnt = 0
for i in range(N-2):
    if S[i] == "#" and S[i+2] == "#" and S[i+1] == ".":
        cnt += 1
print(cnt)