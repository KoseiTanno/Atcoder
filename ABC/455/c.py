# 私の回答
# 不正解
# 辞書を上手に使えるようになってたら、解けてたかもなと感じた
# import copy
# N,K = map(int,input().split())
# A = sorted(list(map(int,input().split())))
# B = copy.deepcopy(A)
# C = set(B)
# D = [0] * len(C)
# B.remove(max(B))
# D[0] = sum(A)-sum(B)
# B.remove(max(B))
# D[1] = (sum(A) - sum(B)) - sum(D)
# B.remove(max(B))
# D[2] = (sum(A) - sum(B)) - sum(D)
# B.remove(max(B))
# D[3] = (sum(A) - sum(B)) - sum(D)
# print(D)
# print(sum(A))

# 模範回答
# collectionsのCounterがまさにこの問題で輝く
# Counterは各値の出現回数を数える辞書
# 入力が1 1 2 2 2 3 なら c = {1: 2, 2: 3, 3: 1}
# つまりこのプログラムの変数cはそれぞれの値を消した場合のそのリストの合計値がどれくらい減るかのリストである(これを作りたかった...)
# その後、cをソートし、末尾からk個消し、消されずに残ったcの合計を出力する
n,k=map(int,input().split())
from collections import Counter
c=Counter(map(int,input().split()))
c=[k*v for k,v in c.items()]
c.sort()
c=c[:-k]
print(sum(c))