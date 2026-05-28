# 私の回答
# 正解
N,D = map(int,input().split())
th_lo = [list(map(int,input().split())) for i in range(N)]
for k in range(1,D+1):
    lst = []
    for th,lo in th_lo:
        lst.append(th*(lo+k))
    print(max(lst))
