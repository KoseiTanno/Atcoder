# https://atcoder.jp/contests/abc381/tasks/abc381_a
# 私の回答
# 正解

N = int(input())
S = input()
M = int(((N+1)/2))
is_odd = N % 2 != 0
is_one = True
is_two = True
is_slash = S[M-1] == "/"
for i in range(N):
    if i < M-1:
        if S[i] != "1":
            is_one = False
    elif i > M-1:
        if S[i] != "2":
            is_two = False
if is_odd&is_one&is_slash&is_two:
    print("Yes")
else:
    print("No")