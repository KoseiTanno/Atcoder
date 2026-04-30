# 私の回答
# 正解
N = int(input())
lst = []
for i in range(1,N+1):
    lst.append(((-1)**i)*(i**3))
print(sum(lst))