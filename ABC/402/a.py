# 私の回答
# 正解
S = input()
N = len(S)
result = ""
for i in range(N):
    if S[i].isupper():
        result += S[i]
print(result)