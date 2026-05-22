N,Q = map(int,input().split())
lst = [0] * N
def ope(kind,num):
    if kind == 1:
        lst[num-1] += 1
        if 0 not in lst:
            for i in range(N):
                lst[i] -= 1
        return
    elif kind == 2:
        cnt = 0
        for i in lst:
            if i >= num:
                cnt += 1
        return cnt
for i in range(Q):
    kind,num = map(int,input().split())
    if kind == 2:
        print(ope(kind,num))
    elif kind == 1:
        ope(kind,num)
