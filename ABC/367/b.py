# https://atcoder.jp/contests/abc367/tasks/abc367_b
# 私の回答
# 正解

X = input()
N = len(X)
for i in range(N-1,0,-1):
    if X[i] == "0":
        X = X[:i]
    else:
        break
    N = len(X)

if "." == X[-1]:
    print(X[:-1])
else:
    print(X)