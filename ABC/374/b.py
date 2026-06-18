# https://atcoder.jp/contests/abc374/tasks/abc374_b
# 私の回答

S = input()
T = input()
N = len(S)
K = len(T)
for i in range(min(N,K)):
    if S[i] != T[i]:
        print(i+1)
        exit()
if N == K:
    print(0)
else:
    print(i+2)

    