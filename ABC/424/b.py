# 私の回答
# 正解
N,M,K = map(int,input().split())
result = {i+1: 0 for i in range(N)}
fastest = False
ranking = []
for i in range(K):
    A,B = map(int,input().split())
    result[A] += 1
    if result[A] == M and not fastest:
        fastest = A
        ranking.append(A)
    elif result[A] == M and fastest:
        ranking.append(A)
print(*ranking)

    