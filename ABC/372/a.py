# https://atcoder.jp/contests/abc372/tasks/abc372_a
# 私の回答
# 正解

S = list(input())
cnt = S.count(".")
for i in range(cnt):
    S.remove(".")
print("".join(S))