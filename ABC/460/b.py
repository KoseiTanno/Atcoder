import math
T = int(input())
lst = [list(map(int,input().split())) for i in range(T)]
for i in range(T):
    dist = (lst[i][3]-lst[i][0])**2 + (lst[i][4]-lst[i][1])**2
    R1 = lst[i][2]
    R2 = lst[i][5]
    if (R1-R2)**2 <= dist <= (R1+R2)**2:
        print("Yes")
    else:
        print("No")
