# 私の回答
# 正解
N = int(input())
login = False
cnt = 0
for i in range(N):
    S = input()
    if S == "login":
        login = True
    elif S == "logout":
        login = False
    elif (not login) and (S == "private"):
        cnt += 1
print(cnt)