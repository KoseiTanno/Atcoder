N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 10000000000
for start in (0,1):
    cnt = (start != A[0])
    cur = start
    for i in range(N-1):
        nxt = (B[i] - cur) % M
        cnt += (nxt != A[i+1])
        cur = nxt
    ans = min(cnt,ans)
print(ans)