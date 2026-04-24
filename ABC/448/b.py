# 私の回答
# 正解
# N,M = map(int,input().split())
# C = list(map(int,input().split()))
# pepper_sum = 0
# for i in range(N):
#     A,B = map(int,input().split())
#     if C[A-1] >= B:
#         pepper_sum += B
#         C[A-1] -= B
#     else:
#         pepper_sum += C[A-1]
#         C[A-1] = 0
# print(pepper_sum)