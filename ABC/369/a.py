# https://atcoder.jp/contests/abc369/tasks/abc369_a
# 私の回答
# 正解

A,B = map(int,input().split())
diff = abs(A-B)
if diff % 2 == 0:
    if diff == 0:
        print(1)
        exit()
    else:
        print(3)
        exit()
else:
    print(2)
