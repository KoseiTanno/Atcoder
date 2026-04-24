# 私の回答
# 正解
# 割と詰まることなくいけた
# B問題も安定して解けるようになってきた
# for文を使わずに要素一個ずつ改行しながらprintする方法がわからなかった
# count_listに最初に部署の数の分の0を入れておくという工夫をした
N,M = map(int,input().split())
count_list = [0 for i in range(N-1)]
for i in range(N):
    A,B = map(int,input().split())
    if A != B:
        count_list[A-1] -= 1
        count_list[B-1] += 1
for i in range(M):
    print(count_list[i])

# 模範回答
# 要素分の0のリストを作るというのを[0]*mとかけることを知らなかった
# 他はほぼ同じ。
n,m = list(map(int,input().split()))
a = [0]*m
for i in range(n):
  u,v = list(map(int,input().split()))
  a[u - 1] -= 1
  a[v - 1] += 1
for y in a:
  print(y)