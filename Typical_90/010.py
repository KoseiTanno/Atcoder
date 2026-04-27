# 私の回答
# 正解
# N = int(input())
# cum1 = [0] * (N+1)
# cum2 = [0] * (N+1)

# for i in range(1,N+1):
#     c,p = map(int,input().split())
#     cum1[i] = cum1[i-1] + (p if c == 1 else 0)
#     cum2[i] = cum2[i-1] + (p if c == 2 else 0)

# Q = int(input())
# for _ in range(Q):
#     l, r = map(int,input().split())
#     print(cum1[r]-cum1[l-1],cum2[r]-cum2[l-1])