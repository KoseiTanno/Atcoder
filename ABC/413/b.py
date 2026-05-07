# 私の回答
# 正解
# まだresultのリストにないときは追加じゃなくて、resultを集合にしていつでも追加すれば、処理時間が減る
N = int(input())
S = [input() for _ in range(N)]
result = set()
for i in range(N):
    for j in range(N):
        if j == i:
            continue
        else:
            result.add(S[i]+S[j])
print(len(result))