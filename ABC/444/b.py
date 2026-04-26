# 私の回答
# 正解
# N,K = map(int,input().split())
# cnt = 0
# for i in range(N+1):
#     total = []
#     for j in range(len(str(i))):
#         total.append(int(str(i)[j]))
#     if sum(total) == K:
#         cnt += 1
# print(cnt)

# 模範回答
# map(int,str(i))とすればそれぞれの桁の数字のリストができる
# それぞれの桁の数字に対してなんらかの処理をしたいときにはそれを使う
N,K=map(int,input().split())
count=0
for i in range(1,N+1):
  if sum(map(int,str(i)))==K:
    count+=1
print(count)
        
