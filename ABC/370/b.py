# https://atcoder.jp/contests/abc370/tasks/abc370_b
# 私の回答
# 正解

N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
cur=0
for x in range(N):
    i=cur
    j=x
    if i>=j: cur=A[i][j]-1
    else: cur=A[j][i]-1
print(cur+1)