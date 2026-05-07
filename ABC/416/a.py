# 私の回答
# 正解
N,L,R = map(int,input().split())
S = input()
if S[L-1:R] == "o" * (R-L+1):
    print("Yes")
else:
    print("No")