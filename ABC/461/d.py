H,W,K = map(int,input().split())
S = [[int(i) for i in list(input())] for _ in range(H)]
print(S)
cnt = 0
for i in range(H):
    for j in range(W):
        cnt_tmp = 0
        for k in range(i,H):
            for l in range(j,W):
                for m in range(H-1,i,-1):
                    for n in range(W-1,j,-1):
                        if sum(S[k:m][l:n]) == K:
                            cnt += 1
        if cnt_tmp == K:
            cnt += 1
print(cnt)
