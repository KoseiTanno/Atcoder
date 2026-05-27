# 私の回答
# 正解
N = int(input())
see = list(map(int,input().split()))
zekken = list(map(int,input().split()))
num = [i for i in range(1,N+1)]
num_zekken = {key:val for key,val in zip(num,zekken)}
res = []
see_zekken = {key:val for key,val in zip(see,zekken)}
see_zekken = dict(sorted(see_zekken.items(),key=lambda x:x[1]))
for i in see_zekken.keys():
    res.append(num_zekken[i])
print(*res)