# 私の回答
# 正解
# for文の繰り返し終了値はiにその値が入った時点で終了するということを途中で思い出した。
# print関数は最後が改行されて終わっていないとターミナルで%が表示されるというのを知らなくて少し戸惑った。
N = int(input())
for i in range(N,0,-1):
    if i == 1:
        print(i)
    else:
        print(i,end=",")
    
# 模範回答
# for文の終了値を1にすることでif文をつけないのスマートだなあ
for i in range(int(input()), 1, -1):
  print(i, end=',')
print(1)