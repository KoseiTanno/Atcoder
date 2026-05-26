# 私の回答
# 正解
N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
i = 0
j = 0
lst = []
while i <= N:
    if j < M:
        if A[j] == i:
            i += 1
            j += 1
        elif A[j] > i:
            for k in range(i+1,A[j]):
                lst.append(k)
            i = A[j]
            j += 1
    else:
        if A[j-1] <= i:
            for k in range(i+1,N+1):
                lst.append(k)
            break
print(len(lst))
print(*lst)