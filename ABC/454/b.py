# 私の回答
# 正解
N,M = map(int,input().split())
F = list(map(int,input().split()))
for i in F:
    if F.count(i) > 1:
        print("No\n")
        break
    elif i == F[-1]:
        print("Yes\n")
for i in range(1,M+1):
    if i not in F:
        print("No")
        break
    else:
        if i == M:
            print("Yes")
