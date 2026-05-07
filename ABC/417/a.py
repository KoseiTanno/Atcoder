# 私の回答
# 正解
N,A,B = map(int,input().split())
S = input()
if A == B == 0:
    print(S)
    exit()
for i in range(A):
    S = S[1:]
for i in range(B):
    S = S[:-1]
print(S)