# 私の回答
# 正解
Q = int(input())
query = [input() for _ in range(Q)]
bag = []
for i in range(Q):
    if len(query[i]) >= 3:
        a,b = map(int,query[i].split())
        bag.append(b)
    else:
        print(min(bag))
        bag.remove(min(bag))
