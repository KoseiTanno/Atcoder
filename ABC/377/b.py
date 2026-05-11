# https://atcoder.jp/contests/abc377/tasks/abc377_b
# 私の回答

N = 8
S = []
cnt = 0
out_row = set()
out_col = set()
for i in range(N):
    S.append(input())
for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            out_row.add(i)
            out_col.add(j)
for i in range(N):
    for j in range(N):
        if (S[i][j] == ".") and (i not in out_row) and (j not in out_col):
            cnt += 1
print(cnt)