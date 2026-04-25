# 私の回答
# 正解
# H,W = map(int,input().split())
# grid = []
# count = 0
# for i in range(H):
#     grid.append(input())
# for h1 in range(H):
#     for h2 in range(h1,H):
#         for w1 in range(W):
#             for w2 in range(w1,W):
#                 is_symmetric = True 
#                 for i in range(h1,(h1+h2) // 2+1):
#                     for j in range(w1,w2+1):
#                         sym_i,sym_j = h2-(i-h1),w2-(j-w1)
#                         if grid[i][j] != grid[sym_i][sym_j]:
#                             is_symmetric = False
#                             break
#                     if not is_symmetric:
#                         break
#                 if is_symmetric:
#                     count += 1
# print(count)

# 模範回答
# スライスはstartから始まりstopの手前で終わる
# [0:3]という表記は最初から2番目まで
# [2:]という表記は二番目から最後まで
# [:]という表記は全部
# [:3]という表記は最初から2番目まで
# [::-1]という表記は逆順
# [x:y][::-1]という表記はx番目からy番目の手前までスライスした後に逆順
# つまりどちらも逆順にすることで点対称のリストを作り出せる
H,W=map(int, input().split())
S = [input() for _ in range(H)]
ans=0
for x2 in range(H+1):
  for x1 in range(x2):
    for y2 in range(W+1):
      for y1 in range(y2):
        if [s[y1:y2] for s in S[x1:x2]] == [s[y1:y2][::-1] for s in S[x1:x2][::-1]]:
          ans+=1
print(ans)