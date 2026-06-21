# https://atcoder.jp/contests/abc373/tasks/abc373_b
# 私の回答
# 正解

S = input()
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cost = 0
cur = Alphabet[0]
i = 1
while(cur != "Z"):
    cost += abs(S.index(cur)-S.index(Alphabet[i]))
    cur = Alphabet[i]
    i += 1
print(cost)