# 私の回答
# 正解
# popは取り出す位置を引数で指定できる
N = int(input())
A = list(map(int,input().split()))
lst = [i for i in range(1,N+1)]
result = [-1] * N
for i in range(N):
    if A[i] in lst:
        result[i] = A[i]
        lst.remove(A[i])
    elif A[i] == -1:
        pass
    else:
        print("No")
        exit()
for i in range(N):
    if result[i] == -1:
        if lst:
            result[i] = lst.pop(0)
        else:
            print("No")
            exit()
print("Yes")
print(*result)