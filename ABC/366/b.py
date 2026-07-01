# https://atcoder.jp/contests/abc366/tasks/abc366_b
# 私の回答
# 正解
# 転置
# 列の最大要素数にサイズを合わせるために"*"を入れるが、行の最後の要素が"*"にならないようにする

N = int(input())
S = [input() for _ in range(N)]
M = max(len(i) for i in S)

for j in range(M):
    row = []
    for i in range(N-1,-1,-1):
        row.append(S[i][j] if j < len(S[i]) else "*")
    print(''.join(row).rstrip("*"))