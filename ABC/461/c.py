N,K,M = map(int,input().split())
co_val = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:x[1],reverse=True)
cnt = 0
col_lst = set()
sum = 0
i = 0
while cnt < K:
    co = co_val[i][0]
    val = co_val[i][1]
    cnt_c = len(col_lst)
    if (M - cnt_c) < (K - cnt):
        col_lst.add(co)
        sum += val
        i += 1
        cnt += 1
        continue
    elif co not in col_lst:
        col_lst.add(co)
        sum += val
        i += 1
        cnt += 1
        continue
    else:
        i += 1
print(sum)
        
