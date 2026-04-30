# 私の回答
# 正解
# 関数定義してみた
N = int(input())
result = 0
i = 0

def num_line(x):
    if x == 0:
        return 1
    else:
        lst = list(map(int,str(x)))
        return sum(lst)

for _ in range(N):
    result += num_line(i)
    i = result
print(result)

