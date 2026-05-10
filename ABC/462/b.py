# 私の回答
# 正解

N = int(input())
give_num_lst = [0] * N
give_from = [[] for _ in range(N)]
for i in range(N):
    a = list(map(int,input().split()))
    for j in range(1,a[0]+1):
        give_num_lst[a[j]-1] += 1
        give_from[a[j]-1].append(i+1)
for i in range(N):
    print(give_num_lst[i],*give_from[i])