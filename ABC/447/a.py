# 私の回答
# ちょっと手こずった
# 隣の席を空けるという処理をどう落とし込むかで迷った
# N,M = map(int,input().split())
# if (N%2 == 0 and M <= N/2) or (N%2 == 1 and M <= (N//2)+1):
#     print("Yes" )
# else:
#     print("No")

# 模範回答
# 偶数と奇数で処理を分ける必要なかったことに気づいた
# どちらも切り捨てにしてしまえばよかった
n, m = map(int, input().split())

if (n+1)//2 >= m:
  print("Yes")
else:
  print("No")