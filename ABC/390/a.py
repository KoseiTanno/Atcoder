# 私の回答
# 正解
# 隣り合う要素というのを見逃していた
A = list(map(int,input().split()))
N = len(A)
lst = [i for i in range(1,N+1)]
cnt = 0
for i in range(N):
    if A[i] != lst[i] and abs(A[i]-lst[i]) == 1:
        cnt += 1
    elif A[i] != lst[i] and abs(A[i]-lst[i]) > 1:
        print("No")
        exit()
if cnt == 2:
    print("Yes")
else:
    print("No")