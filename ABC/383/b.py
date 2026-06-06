# https://atcoder.jp/contests/abc383/tasks/abc383_b
# 私の回答
# 不正解
# H,W,D = map(int,input().split())
# S = [list(input()) for i in range(H)]
# print(S)
# for i in range(H):
#     for j in range(W):


# 模範回答
h,w,d = map(int,input().split())
s = [input() for _ in range(h)]
ans = 0
for hi in range(h):
    for wi in range(w):
        for hj in range(h):
            for wj in range(w):
                if hi == hj and wi == wj:
                    continue
                if s[hi][wi] == "#" or s[hj][wj] == "#":
                    continue
                cnt = 0
                for r in range(h):
                    for c in range(w):
                        if s[r][c] == "#":
                            continue
                        if abs(hi-r) + abs(wi-c) <= d or abs(hj-r) + abs(wj-c) <= d:
                            cnt += 1
                ans = max(ans, cnt)
print(ans)