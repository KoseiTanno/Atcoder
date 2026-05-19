# 私の回答
# 20分以内に解法が思いつかなかった
# N,L = map(int,input().split())
# K = int(input())
# A = list(map(int,input().split()))
# lst = []
# cnt = 0
# dist = 10**9
# for _ in range(K):
#     for j in range(N):
#         goal = L//K
#         tmp = abs((L//K)-min(L-A[j],A[j]))
#         if tmp < dist:
#             dist = tmp
#     lst.append(A[j])
# print(lst)

# 模範回答
# cut_posで先端と末尾を含めた切れ込みの位置のリストを作ることによって、隣り合う要素の引き算だけで、すべてのピースの長さを計算できるようにする
# N, L = [int(s) for s in input().split()]
# K = int(input())
# A = [int(s) for s in input().split()]

# 切れ込みの部分 (先頭と末尾も含める)
# cut_pos = [0] + A + [L]

# ピースが指定した値以上の長さになるなら切れ込みを入れていく。
# 指定した値でK+1このピースに分けることができるならTrueを返す
# def is_valid(mid):
#     piece = 0
#     curr = 0
#     for pos in cut_pos:
#         if pos - curr >= mid:
#             piece += 1
#             curr = pos
#     return piece >= K + 1

# 1ピースの長さが何[cm]かで二分探索
# ok, ng = 0, L + 1
# while ng - ok > 1:
#     mid = (ok + ng) // 2
    
#     if is_valid(mid):
#         ok = mid
#     else:
#         ng = mid

# 最短で ok [cm] になる
# print(ok)

# 模範回答を踏まえた私の回答
# 正解
# 二分探索を覚えた
N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))
cut_pos = [0] + A + [L]

def is_ok(mid):
    piece = 0
    current_pos = 0
    for i in range(N+2):
        if cut_pos[i] - current_pos >= mid:
            piece += 1
            current_pos = cut_pos[i]
    return piece >= K+1

ok,ng = 0,L+1
while ng - ok > 1:
    mid = (ng+ok)//2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)