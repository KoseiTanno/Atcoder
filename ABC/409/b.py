# 私の回答
# 正解
# 最初の回答では実行時間が長すぎる上にメモリ制限超過も起きていたので、改良した
N = int(input())
A = list(map(int,input().split()))
lst = []
for i in range(N+1):
    cnt = 0
    for j in range(N):
        if i <= A[j]:
            cnt += 1
    lst.append(cnt)
for i in range(N+1):
    if lst[i] >= i:
        result = i
print(result)