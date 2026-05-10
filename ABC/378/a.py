# https://atcoder.jp/contests/abc378/tasks/abc378_a
# 私の回答
# 正解

A = list(map(int,input().split()))
B = set(A)
cnt = 0
for i in B:
    cnt += A.count(i) // 2
print(cnt)