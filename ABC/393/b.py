# 私の回答
# 正解
S = input()
N = len(S)
target = "ABC"
cnt = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if j-i == k-j:
                if (S[i] == target[0]) and (S[j] == target[1]) and (S[k] == target[2]):
                    cnt += 1
print(cnt)
