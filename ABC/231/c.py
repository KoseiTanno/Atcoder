import bisect

N,Q = map(int,input().split())
A = sorted(list(map(int,input().split())))
for _ in range(Q):
    x = int(input())
    j = bisect.bisect_left(A,x)
    print(N-j)