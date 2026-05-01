# 私の回答
# 正解
from collections import Counter
a = Counter(map(int,input().split()))
for key,value in a.items():
    if value >= 2:
        print("Yes")
        exit()
print("No")