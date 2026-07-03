X,Y,L,R,A,B = map(int,input().split())
if L <= A < B <= R:
    print(X*(B-A))
elif A < L < B <= R:
    print((L-A)*Y+(B-L)*X)
elif A < L < R < B:
    print((R-L)*X+(L-A+B-R)*Y)
elif L <= A < R < B:
    print((B-R)*Y+(R-A)*X)
else:
    print((B-A)*Y)