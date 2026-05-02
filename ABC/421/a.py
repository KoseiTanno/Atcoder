# 私の回答
# 正解
N = int(input())
S = {i+1:input() for i in range(N)}
X,Y = input().split()
X = int(X)
if S[X] == Y:
    print("Yes")
else:
    print("No")