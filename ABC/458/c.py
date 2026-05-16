# 私の回答
# 正解
S = input()
N = len(S)
cnt = 0
target = "C"
for i in range(N):
    if S[i] == target:
        cnt += min(N-i-1,i)+1
print(cnt)