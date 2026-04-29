# 私の回答
# 正解
# N,M = map(int,input().split())
# S = []
# lst = []
# for i in range(N):
#     S.append(list(input()))
# for i in range(N-M+1):
#     for j in range(N-M+1):
#         tmp_lst = []
#         for k in range(M):
#             for l in range(M):
#                 tmp_lst.append(S[i+k][j+l])
#         if tmp_lst not in lst:
#             lst.append(tmp_lst)
# print(len(lst))
                
# 模範回答
# setに追加するにはappendではなく,addで追加
N,M=map(int,input().split())
S=[input() for _ in range(N)]
grid_set=set()
for i in range(N-M+1):
  for j in range(N-M+1):
    grid = tuple(S[ii][j:j+M] for ii in range(i,i+M))
    grid_set.add(grid)
print(len(grid_set))