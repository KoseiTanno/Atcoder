# https://atcoder.jp/contests/abc371/tasks/abc371_b
# 私の回答

N,M = map(int,input().split())
house_sex = list(map(int,"0" * N))
for i in range(M):
    A,B = input().split()
    A = int(A)
    if B == "M" and house_sex[A-1] == 0:
        print("Yes")
        house_sex[A-1] = 1
    else:
        print("No")