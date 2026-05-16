# 私の回答
# 正解
# [:-K]は末尾からKこの要素を取り除いた残りの部分
N,K = map(int,input().split())
A = sorted(list(map(int,input().split())))
from collections import Counter
print(sum(sorted([a*b for a,b in Counter(A).items()])[:-K]))