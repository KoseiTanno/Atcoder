# https://atcoder.jp/contests/abc378/tasks/abc378_b
# 私の回答

N = int(input())
divideByList = []
remList = []
for i in range(N):
    divideBy,rem = map(int,input().split())
    divideByList.append(divideBy)
    remList.append(rem)
Q = int(input())
for i in range(Q):
    kind,day = map(int,input().split())
    if day <= remList[kind-1]:
        print(remList[kind-1])
    else:
        number = remList[kind-1] + divideByList[kind-1]
        while number <= day:
            number += divideByList[kind-1]
        print(number)
        


