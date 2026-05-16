N = int(input())
A = list(map(int,input().split()))
result = 0
for i in range(N):
    for j in range(N):
        if j != i:
            result += A[i]*A[j]
print(result//2)