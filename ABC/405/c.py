# 私の回答
# 正解
# 一回全てを掛け合わせたものを作って、後から過剰分を引く
N = int(input())
A = list(map(int,input().split()))
total = sum(A)*sum(A)
total -= sum([i*i for i in A])
print(total//2)