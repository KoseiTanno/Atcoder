# 私の回答
# 正解
# if文で二つの条件文を&で繋げる時にそれぞれの条件文の適切なところにカッコを入れないと当然だがうまく機能しない
# N,M = map(int,input().split())
# S = [input() for _ in range(N)]
# cnt_lst = [0] * M
# for i in range(M):
#     for j in range(N):
#         if int(S[j][i]) == 0:
#             cnt_lst[i] -= 1
#         elif int(S[j][i]) == 1:
#             cnt_lst[i] += 1
# score_lst = [0] * N
# for i in range(N):
#     for j in range(M):
#         if cnt_lst[j] == N or cnt_lst[j] == -N:
#             score_lst[i] += 1
#             continue
#         elif (cnt_lst[j] > 0) & (int(S[i][j]) == 0):
#             score_lst[i] += 1
#             continue
#         elif (cnt_lst[j] < 0) & (int(S[i][j]) == 1):
#             score_lst[i] += 1
#             continue
# lst = []
# for i in range(N):
#     if score_lst[i] == max(score_lst):
#         lst.append(i+1)
# print(*lst)

# 模範回答
