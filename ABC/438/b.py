# 私の回答
# 不正解
# 時間内に解けなかった。
# 数時間の距離をどう表すかということと、部分文字列にするための最小の時間をどうやって計算すれば良いかがわからなかった
# N,M = map(int,input().split())
# S = input()
# T = input()
# cnt = 0
# while(1):
#     if T in S:
#         print(cnt)
#         exit()
#     for i in 

# 模範回答
# tをsの上でスライドさせながら全位置を試す
# それぞれの位置でのコストを計算して比較する
# %10だと、sが0でtが9の時コストが1になる。
n,m=map(int,input().split())
s=input()
t=input()
ans=10**9
for st in range(n-m+1):
    res=0
    for i in range(m):
        res+=(int(s[st+i])-int(t[i]))%10
    ans=min(ans,res)
print(ans)