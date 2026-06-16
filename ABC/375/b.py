# https://atcoder.jp/contests/abc375/tasks/abc375_b
# 私の回答
# 正解
import math

N = int(input())
total_cost = 0
pos_lst = [[0,0]]
for i in range(N):
    X,Y = map(int,input().split())
    pos_lst.append([X,Y])
pos_lst.append([0,0])
for i in range(1,N+2):
    cost = math.sqrt((pos_lst[i-1][0]-pos_lst[i][0])**2+((pos_lst[i-1][1]-pos_lst[i][1])**2))
    total_cost += math.sqrt((pos_lst[i-1][0]-pos_lst[i][0])**2+((pos_lst[i-1][1]-pos_lst[i][1])**2))
    pre_X,pre_Y = X,Y
print(total_cost)

