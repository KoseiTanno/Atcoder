# 私の回答
# 正解
# 実行時間が長い
# H,W = map(int,input().split())
# A = [list(map(int,input().split())) for _ in range(H)]
# B = [[0] * W for _ in range(H)]
# row_sum = [sum(A[i]) for i in range(H)]
# col_sum = [sum(A[i][j] for i in range(H)) for j in range(W)]
# for i in range(H):
#     for j in range(W):
#         B[i][j] = row_sum[i] + col_sum[j] - A[i][j]
# for i in range(H):
#     print(*B[i])

# 模範回答
# 
h, w = map(int, input().split())
a = []
a1= []
a2= [0] * w
for i in range(h):
  a.append(list(map(int, input().split())))
  a1.append(sum(a[-1]))
  for i in range(w):
    a2[i] += a[-1][i]
for i in range(h):
  b = []
  for j in range(w):
    b.append(str(a1[i] + a2[j] - a[i][j]))
  print(" ".join(b))