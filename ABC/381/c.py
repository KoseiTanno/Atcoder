# https://atcoder.jp/contests/abc381/tasks/abc381_c
# 私の回答
# TLE
# T = int(input())
# S = list(input())

# max_L = 1
# for i in range(T-2):
#     for j in range(i+2,T,+2):
#         L = j-i+1
#         is_one = True
#         is_two = True
#         is_slash = True
#         M = int((L+1)/2)
#         for k in range(i,j+1):
#             if k-i < M-1 and S[k] != "1":
#                 is_one = False
#             elif k-i > M-1 and S[k] != "2":
#                 is_two = False
#             elif k-i == M-1 and S[k] != "/":
#                 is_slash = False
#         if is_one and is_two and is_slash and (max_L < L):
#             max_L = L
# print(max_L)

# 模範回答
N = int(input())
S = input()

left1 = [0] * N
right2 = [0] * N

for i in range(N):
    if S[i] == "1":
        left1[i] = left1[i - 1] + 1 if i > 0 else 1

for i in range(N - 1, -1, -1):
    if S[i] == "2":
        right2[i] = right2[i + 1] + 1 if i < N - 1 else 1

ans = 1

for i in range(N):
    if S[i] == "/":
        l = left1[i - 1] if i > 0 else 0
        r = right2[i + 1] if i < N - 1 else 0
        ans = max(ans, min(l, r) * 2 + 1)

print(ans)