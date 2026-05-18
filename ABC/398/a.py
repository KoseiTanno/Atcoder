# 私の回答
# 正解
N = int(input())
result = "-" * N
center = (N-1)//2
if N % 2 == 0:
    result = result[:center] + "==" + result[center+2:]
else:
    result = result[:center] + "=" + result[center+1:]
print(result)