# 私の回答
# 正解

S = list(input())
N = len(S)
lst = []
for i in range(N):
    if S[i] >= "0" and S[i] <= "9":
        lst.append(S[i])
print("".join(lst))