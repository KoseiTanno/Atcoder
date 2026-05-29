N,M = map(int,input().split())
x = N%M
cnt = 1
while x > 0:
    cnt += 1
    M = x
    x = N%M
print(cnt)