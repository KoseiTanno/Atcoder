# https://atcoder.jp/contests/abc369/tasks/abc369_b
# 私の回答
# 正解

N = int(input())
lst = []
first_L = False
first_R = False
tired = 0
for i in range(N):
    lst.append(list(input().split()))
for i in lst:
    if (i[1] == "L") and (not first_L):
        pre_L = int(i[0])
        first_L = True
    elif (i[1] == "L"):
        tired += abs(pre_L - int(i[0]))
        pre_L = int(i[0])
    elif (i[1] == "R") and (not first_R):
        pre_R = int(i[0])
        first_R = True
    else:
        tired += abs(pre_R - int(i[0]))
        pre_R = int(i[0])
    
print(tired)

