# 私の回答
# 公約数とかいう概念を使うのかなということを考えたが実相が分からず、ACできなかった
# A = int(input())
# B = int(input())
# C = int(input())
# X = int(input())

# coins_a = []
# coins_b = []
# coins_c = []
# coins = [coins_a, coins_b, coins_c]
# for a in range(A):
#     coins_a.append(500*1)
# for b in range(B):
#     coins_b.append(100*1)
# for c in range(C):
#     coins_c.append(50*1)



# 模範回答
# rangeもA+1とすることによって0,1,2,...,Aというように500円だまがある個数と100円だまがある個数を考慮した組み合わせを網羅できる
# AとBの組み合わせを網羅しつつ、それぞれの場面でsumを算出しておくことで、sumがXよりすでに大きい場合を考慮から外す事ができるため計算時間の短縮になる
# ((X-sum)/50 <= C)とかけるのは、Xは50の倍数だからCよりX-sumが小さい時点で50円玉を使ってX-sumにできる事が確定する
A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for i_A in range(A+1):
    for i_B in range(B+1):
        sum = i_A * 500 + i_B * 100
        if (sum <= X) and ((X - sum)/50 <= C):
            count += 1

print(count)