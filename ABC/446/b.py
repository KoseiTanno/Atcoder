# 私の回答
# 正解
# N,M = map(int,input().split())
# juice_list = [i for i in range(1,M+1)]
# ordered_list = []
# for i in range(1,N+1):
#     L = int(input())
#     X = list(map(int,input().split()))
#     for j in range(L):
#         if X[j] in juice_list:
#             ordered_list.append(X[j])
#             juice_list.remove(X[j])
#             break
#         elif (X[j] not in juice_list) and j == L-1:
#             ordered_list.append(0)
# for i in ordered_list:
#     print(i)

# 模範回答
# Trueで埋められたリストを使うという方法は参考になった
# okという仮のフラグを準備してもしまだ希望リストないから注文できてないなら水を注文という処理
N,M=map(int,input().split())
j=[True for i in range(M)]
for _ in range(N):
    L=int(input())
    X=list(map(int,input().split()))
    ok=False
    for i in X:
        if j[i-1]:
            print(i)
            ok=True
            j[i-1]=False
            break
    if not ok:
        print(0)
