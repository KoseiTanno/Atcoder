# 私の回答
# 正解
from collections import Counter
A = list(map(int,input().split()))
B = Counter(A)
three = False
two = False
pre = 0
for key,value in B.items():
    if (value >= 3) and (pre != key) and (three == False):
        three = True
        pre = key
    elif (value >= 2) and (pre != key) and (two == False):
        two = True
        pre = key
    if two and three:
        print("Yes")
        exit()
print("No")