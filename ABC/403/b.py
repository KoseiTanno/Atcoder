# 私の回答
# 正解
T = input()
S = input()
N = len(T)
M = len(S)
for i in range(N-M+1):
    cnt = 0
    if (T[i] in S) or (T[i] == "?"):
        for j in range(M):
            if (T[i+j] == S[j]) or (T[i+j] == "?"):
                cnt += 1
        if cnt == M:
            print("Yes")
            exit()
print("No")
