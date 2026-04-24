# 私の回答
# 正解
# だが40分ぐらいかかった
# countのリストを書き換えていることで、max(count)が変動してしまっていることに気づくことに時間がかかった
# 書き換えてもmaxが変わらないようにdeepcopyを用いた
# 出現頻度の扱い方を知らないことに気づいた
# import copy
# S = input()
# N = len(S)
# count = [0] * N
# for i in range(N):
#     for j in S:
#         if S[i] == j:
#             count[i] += 1
# c_copy = copy.deepcopy(count)
# for i in range(N):
#     if count[i] == max(c_copy):
#         count[i] = 1
#     else:
#         count[i] = 0
# for i in range(N):
#     if count[i] == 0:
#         print(S[i],end="")

# 模範回答
# count関数というものが存在することを知らなかった
# リストやタプル、文字列内で指定した要素が何回出現するかを整数で返す機能
# この問題は辞書で実装すれば楽
s = input()
cnt = {c : s.count(c) for c in s}
ma = max(cnt.values())
print("".join(c for c in s if cnt[c] != ma))