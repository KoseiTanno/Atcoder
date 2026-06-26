# https://atcoder.jp/contests/abc367/tasks/abc367_a
# 私の回答
A,sleep,wake = map(int,input().split())
lst = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
if wake <= A and A <= sleep:
    print("No")
else:
    print("Yes")