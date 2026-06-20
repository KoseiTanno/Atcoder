N,K = map(int,input().split())
L_R = [list(map(int,input().split())) for _ in range(N)]

# 数直線上にN枚の布が区間L,Rを覆い被さるように落ちている
# N枚の中からK枚選ぶようにしたい
# 重なっていない区間の長さの最小値がスコアとして採用される
# N枚の中からどのK枚を選んでも重なっていない区間がない場合は-1を出力する
