# 私の回答
# 正解
import copy
X = list(map(int,str(input())))
X_new = copy.deepcopy(X)
N = len(X)
zero_cnt = 0
for i in range(N):
    if X[i] == 0:
        zero_cnt += 1
for _ in range(zero_cnt):
    X_new.remove(0)
X_new = sorted(X_new)
for _ in range(zero_cnt):
    X_new.insert(1,0)
for i in range(N):
    if i != N-1:
        print(X_new[i],end="")
    else:
        print(X_new[i])
