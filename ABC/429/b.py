# 私の回答
# 正解
N,M = map(int,input().split())
A = list(map(int,input().split()))
lst = []
sum_lst = []
for i in range(N):
    for j in range(N):
        if j != i:
            lst.append(A[j])
    sum_lst.append(sum(lst))
    lst = []
if M in sum_lst:
    print("Yes")
else:
    print("No")