# 私の回答
# 正解
N = int(input())
S = list(input())
while(len(S) < N):
    S.insert(0,"o")
print("".join(S))