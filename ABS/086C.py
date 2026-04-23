# 私の回答
# C問題時間かかったけど正解できた嬉しい
# 移動できる数と時間を導出するときに前の地点を引いて導出しないといけないことを失念していて時間がかかった
# そして、移動できる数的にはいけても止まっていることができないという制約を入れ込むために2で割ったあまりを比較した
# N = int(input())
# time_list = [0]
# action_list = [0,0]
# for i in range(N):
#     t,x,y = map(int,input().split())
#     time_list.append(t)
#     action_list.append(x)
#     action_list.append(y)
#     if (abs(x-action_list[-4])+abs(y-action_list[-3]) <= (t-time_list[-2])) and ((abs(x-action_list[-4])+abs(y-action_list[-3]))%2 == ((t-time_list[-2]))%2):
#         continue
#     else:
#         print("No")
#         exit()
# print("Yes")

# 模範回答
# これを見て確かにリストに追加していく意味はなかったと感じた
# 参照するのは一つ前の場所だけだからだ
# 値を一回しか参照しないときはただの変数でもいいことを覚えておこう、メモリを無駄に使ってしまう
# 他の中身はほとんど一緒だった
n = int(input())
nt, nx, ny = 0, 0, 0
flg = True
for _ in range(n):
    t, x, y = map(int, input().split())
    dis=abs(nx-x)+abs(ny-y)
    if t-nt>=dis and (t-nt-dis)%2==0:
        nt, nx, ny = t, x, y
    else:
        flg = False

print("Yes" if flg else "No")