# 私の回答
# 正解
# だが実行時間が480msで少し長い
# Q = int(input())
# vol = 0
# play = False
# for i in range(Q):
#     A = int(input())
#     if A == 1:
#         vol += 1
#     elif A == 2 and vol >= 1:
#         vol -= 1
#     elif A == 3 and play == True:
#         play = False
#     elif A == 3 and play == False:
#         play = True
#     print("Yes" if vol >= 3 and play else "No")

# 模範回答
# 174ms
# 先に全部入力を受け取ってリストにして、そこから参照する形のほうが早いのか
Q = int(input())
A = [int(input()) for _ in range(Q)]

vol = 0
play = False
for i in range(Q):
  if(A[i] == 1):
    vol += 1
  elif(A[i] == 2):
    if(vol >= 1):
      vol -= 1 
  else:
    play = not play
  
  if(vol >=3 and play):
    print("Yes")
  else:
    print("No")