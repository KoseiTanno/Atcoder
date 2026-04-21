# 私の回答
# T,X = map(int, input().split())
# A = list(map(int,input().split()))
# storage = []
# for i in range(T+1):
#     if i == 0:
#         storage.append(A[0])
#         print(f"{i} {A[i]}")
#     elif abs(A[i] - storage[-1]) >= X:
#         print(f"{i} {A[i]}")
#         storage.append(A[i])

# 模範回答
t,x=map(int,input().split())
a=list(map(int,input().split()))
b=-x
for i in range(t+1):
  if abs(b-a[i])>=x:
    print(i,a[i])
    b=a[i]