# 私の回答
# 正解
N = int(input())
R = [i for i in range(1,N)]
D = list(map(int,input().split()))
a_list = []
b_list = []
for i in range(N):
    if not D[i]:
        a_list.append(i+1)
    else:
        break
for i in range(N-1,0,-1):
    if not D[i]:
        b_list.append(i)
    else:
        break
reached = set(a_list+b_list)
for i in reached:
    if i in R:
        R.remove(i)
print(len(R))