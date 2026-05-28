# 私の回答
# 正解
# 式変形という発想
N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in range(1,N-1):
    if A[i]**2 != A[i-1]*A[i+1]:
        print("No")
        exit()
print("Yes")        