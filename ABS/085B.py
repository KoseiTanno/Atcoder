# 私の回答
# N = int(input())
# d = []
# count = 0
# for i in range(N):
#     tmp = int(input())
#     if not tmp in d: 
#         d.append(tmp)
# d.sort(reverse=True)
# if d:
#     for i in d:
#         count += 1
# print(count)

# 模範回答
# 私も重複を許さないリストまでは作れてたので、そのままそのリストの個数を出力すればよかったことに気づいた
# setというものを知らなかった。重複を許さないデータ構造で、集合のことらしい。便利だな
n = int(input())
d = [int(input()) for _ in range(n)]

print(len(set(d)))