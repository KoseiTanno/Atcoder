# 私の回答
# 正解
from collections import Counter
lst = sorted(list(map(int,input().split())))
dic = Counter(lst)
if len(dic) == 2:
    print("Yes")
else:
    print("No")
