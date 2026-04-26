# 私の回答
# 正解
# N,K = map(int,input().split())
# total = 0
# cnt = 0
# while(total < K):
#     total += N
#     N += 1
#     cnt += 1
# print(cnt-1)

# 模範回答
n,k=map(int,input().split())

i=0
m=0

while m<k:
  m+=n+i
  if m>=k:
    print(i)
  i+=1
