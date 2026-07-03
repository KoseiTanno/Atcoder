N,M = map(int,input().split())
col_max = [-1 for _ in range(M)]
for i in range(N):
    C,S = map(int,input().split())
    if S > col_max[C-1]:
        col_max[C-1] = S
print(*col_max)