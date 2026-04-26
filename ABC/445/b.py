# 私の回答
# 正解
# なんか上手じゃない処理
# N = int(input())
# S = []
# for i in range(N):
#     S.append(input()) 
# long = ""
# for i in S:
#     if len(i) >= len(long):
#         long = i
# for i in S:
#     if long == i:
#         print(i)
#     else:
#         dots_num = (len(long) - len(i)) // 2
#         print((dots_num * ".") + i +(dots_num * "."))

# 模範回答
# listってそのまま使うと予約されている関数名になっちゃうから一文字抜いてlstって変数名使うの脳のリソース使わなくて便利だから真似しよ
# max関数はkeyを指定することができる
# key=lenとすると要素の数で最大のものを取得してきてくれる
N = int(input())
lst = []
for _ in range(N):
  S = input()
  lst.append(S)

m = len(max(lst,key=len))

for i in lst:
  k = (m - len(i)) // 2
  print("." * k + i + "." * k)