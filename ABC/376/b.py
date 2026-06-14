# https://atcoder.jp/contests/abc376/tasks/abc376_b
# 私の回答
# 不正解(20分経過)

# N,Q = map(int,input().split())
# left = ["L",1]
# right = ["R",2]
# cnt = 0
# for i in range(Q):
#     hand,position = input().split()
#     goal = [hand,int(position)]
#     while(goal != left and goal != right):
#         if hand == "L":
#             if abs(position - left[1]):
#         else:
#             if abs(position - right[1]):

N,Q = map(int,input().split())
hands = {"L":0,"R":1}
ans = 0
for _ in range(Q):
    H,T = input().split()
    T = int(T)-1
    other = hands["L" if H == "R" else "R"]
    cur = hands[H]
    cw = (T - cur) % N
    if ((other - cur) % N) < cw:
        ans += (cur - T) % N
    else:
        ans += cw
    hands[H] = T
print(ans)