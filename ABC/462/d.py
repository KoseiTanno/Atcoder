N,D = map(int,input().split())
suspects = []
for _ in range(N):
    S,T = map(int,input().split())
    suspects.append([S,T])
suspects.sort()
ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        S1,T1 = suspects[i]
        S2,T2 = suspects[j]
        start = S2
        end = min(T1,T2) - D
        if start <= end:
            ans += end - start + 1
print(ans)