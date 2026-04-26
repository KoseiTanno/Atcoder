# 私の回答
# 正解
# 解法はすぐ思いついたが、まだ慣れていない辞書を使おうと思ったので、時間がかかった
# 辞書の何番目の値でsortというのはkey = lamda x:x[何番目]で指定できる
# lambdaは無名の関数
# printで出力するときに個数を制限したいときはスライスするといい
N = int(input())
A = list(map(int,input().split()))
T = {i+1: A[i] for i in range(N)}
T = sorted(T.items(),key=lambda x:x[1])
K = [T[i][0] for i in range(N)]
print(*K[:3])
