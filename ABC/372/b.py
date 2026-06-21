# https://atcoder.jp/contests/abc372/tasks/abc372_b
# 私の回答
# 正解
# 3**iのリストを先に準備しておいて、それを指定の数から引ける一番大きい数から引いていくという処理

M = int(input())
lst = [3**i for i in range(11)]
N = len(lst)
lst.reverse()
res = []
i = 0
while(M != 0):
    if M >= lst[i]:
        M -= lst[i]
        res.append(N-i-1)
        i = 0
    else:
        i += 1
print(len(res))
print(*res)