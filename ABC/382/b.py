# https://atcoder.jp/contests/abc382/tasks/abc382_b
# 私の回答
# 正解

N,D = map(int,input().split())
S = list(input())
i = N-1
cnt = 0
while(cnt < D):
    if S[i] == "@":
        cnt += 1
        S[i] = "."
    i -= 1
print("".join(S))