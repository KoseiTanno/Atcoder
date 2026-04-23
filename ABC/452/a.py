# 私の回答
# 正解
# 他の人の回答も確認したがこれが最善ぽいので今回は模範解答はなし
M,D = map(int,input().split())
sekku = [(1,7),(3,3),(5,5),(7,7),(9,9)]
if (M,D) in sekku:
    print("Yes")
else:
    print("No")