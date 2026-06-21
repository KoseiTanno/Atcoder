# 私の回答
# 正解

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(max(A[:N])+max(B[:N]))