# https://atcoder.jp/contests/abc382/tasks/abc382_a
# 私の回答
# 正解

N,D = map(int,input().split())
S = list(input())

print(N-(S.count("@")-D))
