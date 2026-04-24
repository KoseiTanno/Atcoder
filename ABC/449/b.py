# 私の回答
# 正解
# 特に詰まることなくスラスラとけた
# 図を紙に書いたのが考えやすくて良かった
# H,W,Q = map(int,input().split())
# query = []
# for i in range(Q):
#     query.append(list(map(int,input().split())))
# for i in range(Q):
#     if query[i][0] == 1:
#         print(query[i][1] * W)
#         H -= query[i][1]
#     else:
#         print(query[i][1] * H)
#         W -= query[i][1]

# 模範回答
# for文を使用するけどループ変数は内側での処理内容に出てこないときはアンダースコアを使うと変数名を無駄に使用することなくloopが可能だそうだ
# 使わないのに指定するのに違和感があったのでこれから使っていこうと思う
# 2個ループを作らなくても、queryを受け取ってすぐチョコレートを食べることができたことにこれを見て気づいた
H,W,Q = map(int,input().split())
for _ in range(Q):
    t, x = map(int, input().split())

    if t == 2:
        print(H * x)
        W -= x
    else:
        print(W * x)
        H -= x