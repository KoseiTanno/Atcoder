# 私の回答
# 正解
# 特段悪いとこはないがsetを使っている人と比較すると私のコードの実行時間のほうが遅いことからsetを使ったほうがいいことがわかる
N,M = map(int,input().split())
S = input()
T = input()
Q = int(input())
w = [input() for i in range(Q)]
for i in range(Q):
    result = ""
    for j in set(w[i]):
        if j in S and j not in T:
            result = "Takahashi"
        elif j in T and j not in S:
            result = "Aoki"
    if result == "":
        print("Unknown")
    else:
        print(result)
    