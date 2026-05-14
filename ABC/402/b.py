# 私の回答
# 正解
Q = int(input())
lst = []
for i in range(Q):
    tmp = input()
    if len(tmp) >= 2:
        num,X = map(int,tmp.split())
        if num == 1:
            lst.append(X)
        continue
    else:
        if int(tmp) == 2:
            print(lst.pop(0))
