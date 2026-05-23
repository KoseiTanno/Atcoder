# 私の回答
# 正解
Q = int(input())
lst = [0] * 100
for i in range(Q):
    c = input()
    if int(c[0]) == 1:
        a,b = map(int,c.split())
        lst.append(b)
    else:
        print(lst.pop())

