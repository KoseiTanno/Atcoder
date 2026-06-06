# https://atcoder.jp/contests/abc381/tasks/abc381_b
# 私の回答
# 正解

S = list(input())
N = len(S)
S_2 = set(S)
is_even = N % 2 == 0
is_same = True
is_two = True
for i in range(1,int(N/2)):
    if S[2*i-1] != S[2*i-2]:
        is_same = False
for i in S_2:
    if S.count(i) != 2:
        is_two = False
if is_even&is_same&is_two:
    print("Yes")
else:
    print("No")