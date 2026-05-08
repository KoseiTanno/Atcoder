# 私の回答
# 正解
N = int(input())
A = list(map(int,input().split()))
A = sorted(set(A))
print(len(A))
print(*A)