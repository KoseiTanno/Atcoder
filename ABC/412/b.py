# 私の回答
# 正解
S = input()
T = input()
N = len(S)
for i in range(N):
    if (i != 0) and (S[i].isupper()):
        if S[i-1] not in T:
            print("No")
            exit()
print("Yes")