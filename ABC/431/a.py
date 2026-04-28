# 私の回答
# 正解
H,B = map(int,input().split())
cnt = 0
while(H>B):
    B += 1
    cnt += 1
print(cnt)