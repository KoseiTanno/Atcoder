# https://atcoder.jp/contests/abc368/tasks/abc368_b
# 私の回答
# 正解
N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
cnt = 0
while(A[0] > 0 and A[1] > 0):
    A[0] -= 1
    A[1] -= 1
    cnt += 1
    A.sort(reverse=True)
print(cnt)