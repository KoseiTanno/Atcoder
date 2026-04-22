# 私の回答
# なんとか正解出来たがかなり時間がかかってしまった。
# しかし我ながら良い発想のコードが書けたと思う
# 三重ループを二重ループに直したのと、rangeを工夫したのが良かった。
# あと、リストに対して最初に＊をつけると中身を出してくれるらしい
# N,Y = map(int,input().split())
# result = []
# Y = Y/1000
# for x in range(N+1):
#     for y in range(N+1-x):
#         total = 10*x + 5*y
#         if Y-total == N-x-y:
#             result.append([x,y,N-x-y])
#             print(*result[0])
#             exit()
# if not result:
#     print(-1,-1,-1)

# 模範回答
# exit()はプログラムを終了する事ができる。
# 三重ループになりそうな時は本当に三重にする必要があるのかを一度考える
n,y=map(int,input().split())

for i in range (n+1):
  for j in range (n+1-i):
    k=n-i-j
    if 10000*i+5000*j+1000*k==y:
      print(i,j,k)
      exit()

print(-1,-1,-1)
    