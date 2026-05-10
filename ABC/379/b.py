# https://atcoder.jp/contests/abc379/tasks/abc379_b
# 私の回答
# 正解

N,K = map(int,input().split())
S = input()
seq_cnt = 0
seq_lst = []
for i in range(N):
    if S[i] == "O" and i == N-1:
        seq_cnt += 1
        seq_lst.append(seq_cnt)
        break
    elif S[i] == "O":
        seq_cnt += 1
    else:
        seq_lst.append(seq_cnt)
        seq_cnt = 0
cnt = 0
for i in seq_lst:
    while i >= K:
        i -= K
        cnt += 1
print(cnt)
        
    