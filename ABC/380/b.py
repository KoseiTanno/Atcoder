# https://atcoder.jp/contests/abc380/tasks/abc380_b
# 私の回答
# 正解

S = input()

N = len(S)
i = 0
cnt_lst = []
while i < N-1:
    if S[i] == "|":
        i += 1
        cnt = 0
        while S[i] != "|":
            cnt += 1
            i += 1
        cnt_lst.append(cnt)
    else:
        i += 1
print(*cnt_lst)