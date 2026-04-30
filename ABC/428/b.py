# 私の回答
# 正解
# from collections import Counter
# N,K = map(int,input().split())
# S = input()
# lst = []
# new_lst = []
# for i in range(N-K+1):
#     lst.append(S[i:i+K])
# result = Counter(lst).most_common() 
# result = sorted(result,key = lambda x:(-x[1],x[0]))
# print(result[0][1])
# for i,j in result:
#     if j == result[0][1]:
#         new_lst.append(i)
# print(*new_lst)

# 模範回答
# defaultdict(int)は存在しないキーにアクセスした時自動で0を初期値にしてくれる辞書
# 引数として(list)を渡すと存在しないキーにアクセスした時[]を返す
# strだと""
# 要素数分の0が入ったリストを準備しなくてよくて便利
# 0から数え始められる
from collections import defaultdict

N, K = map(int, input().split())
S = input()

count = defaultdict(int)

for i in range(N - K + 1):
    t = S[i:i+K]
    count[t] += 1

max_count = max(count.values())

ans = []
for key, value in count.items():
    if value == max_count:
        ans.append(key)

ans.sort()

print(max_count)
print(*ans)