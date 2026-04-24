# 私の回答
# 不正解
# というか回答すらできず
# 乗り継ぎをどうやって表せばいいかわからなかった
# N = int(input())
# C = []
# for i in range(N-1):
#     C.append(list(map(int,input().split())))
# for i in range(N-1):
#     cost_sum = 0
#     for j in range(1,N-1):
#         cost_sum == C[i][j-1] +
#         if cost_sum ==  C[i][j]
# print(C)

# 模範回答
# 美しい。
# 与えられた要件を数式に直してからそれをコードに落とし込めば良いと感じた
# 三つの整数a,b,cがそれぞれ可変だったので、三重ループにするしかない
# ゼロパディングでインデックスのズレを直すというテクニックを知った
# 
n=int(input())
g=[[0]*(i+1)+list(map(int,input().split())) for i in range(n-1)]
for a in range(n):
  for b in range(a+1,n):
    for c in range(b+1,n):
      if g[a][b]+g[b][c]<g[a][c]:
        print("Yes")
        exit()
print("No")