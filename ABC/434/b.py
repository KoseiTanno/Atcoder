# 私の回答
# 正解
# 小数点以下何桁まで表示するかは"{:.10f}".format(x)というようにすればいじることができる
# 辞書型を使おうと思っていたが、結局リストを二つ作ってそれを一つのリストにしても同じことだと思った
# 処理順がうまく実装できないときはとりあえずソートするといい
N,M = map(int,input().split())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
AB = list(zip(A,B))
AB = sorted(AB)
CD = [0] * M
cnt = [0] * M
for i in range(N):
    for j in range(M):
        if AB[i][0] == j+1:
            CD[j] += AB[i][1]
            cnt[j] += 1
for i in range(M):
    ave = CD[i]/cnt[i]
    result = "{:.20f}".format(ave)
    print(result)
            
