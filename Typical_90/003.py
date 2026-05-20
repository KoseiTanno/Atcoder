# 私の回答
# 20分以内に回答が実装できなかった
# N = int(input())
# costs = [0] * N
# for i in range(N-1):
#     A,B = map(int,input().split())
#     if A == 1:
#         costs[B-1] = 1
#     else:
#         costs[B-1] += 1
# print(costs)

# def calc(A,B):
#     if A == 1:
#         return 1
#     else:
#         costs[A-1] += 1
#         calc(A-1,B)

# 模範回答
# BFSを2回やる
# from collections import deque

# n = int(input())
# graph = [[] for _ in range(n)]

# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     a -= 1; b -= 1
#     graph[a].append(b); graph[b].append(a)

# 最大値のindexを求める関数
# def max_ind(a):
#     m = a[0]; ans = 0
#     for i in range(1, len(a)):
#         if m < a[i]:
#             m = a[i]; ans = i
#     return ans

# BFSをして(最大値, index)を返す関数
# def bfs(s):
#     dist = [-1] * n
#     work = deque([s])
#     dist[s] = 0
#     while work:
#         x1 = work.popleft()
#         for x2 in graph[x1]:
#             if dist[x2] < 0:
#                 dist[x2] = dist[x1] + 1
#                 work.append(x2)
#     return max(dist), max_ind(dist)

# im = bfs(0)[1]
# print(bfs(im)[0] + 1)

# 模範回答を踏まえた私の回答
# 正解
# 幅優先探索の基本の実装を覚えた
from collections import deque
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a -= 1;b -= 1
    graph[a].append(b);graph[b].append(a)

def max_ind(a):
    m = a[0] ; ans = 0
    for i in range(1,n):
        if m < a[i]:
            m = a[i];ans = i
    return ans

def bfs(s):
    dist = [-1] * n
    work = deque([s])
    dist[s] = 0
    while work:
        x1 = work.popleft()
        for x2 in graph[x1]:
            if dist[x2] < 0:
                dist[x2] = dist[x1] + 1
                work.append(x2)
    return max(dist),max_ind(dist)

im = bfs(0)[1]
res = bfs(im)[0] + 1
print(res)