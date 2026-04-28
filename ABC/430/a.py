# 私の回答
# 正解
A,B,C,D = map(int,input().split())
if C >= A:
    if B > D:
        print("Yes")
        exit()
print("No")