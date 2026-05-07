# 私の回答
# 正解
N = int(input())
S = []
for i in range(N):
    a,b = input().split()
    b = int(b)
    if b > 100:
        print("Too Long")
        exit()
    S.append(a*b)
long = len("".join(S))
if long > 100:
    print("Too Long")
else:
    print("".join(S))