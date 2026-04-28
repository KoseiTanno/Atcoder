# 私の回答
# 正解
N = int(input())
cnt = 0
result = []
A = list(map(int,input().split()))
cnt = 0
for l in range(N-1):
    for r in range(l+1,N):
        ok = False
        s = sum(A[l:r+1])
        for i in range(l,r+1):
            if s%A[i] == 0:
                ok = False
                break
            else:
                ok = True
        if ok:
            cnt += 1
print(cnt)