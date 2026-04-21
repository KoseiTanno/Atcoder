# 自分の回答
# ほとんど詰まることなく実行時間も早い回答ができて良かった
# N = int(input())
# a = list(map(int,input().split()))
# alice_score = 0
# bob_score = 0
# for i in range(0,N,2):
#     if len(a) >= 2:
#         alice_score += max(a)
#         a.remove(max(a))
#         bob_score += max(a)
#         a.remove(max(a))
#     else:
#         alice_score += max(a)

# print(alice_score - bob_score)

# 模範回答
# この回答を見てsortすればremoveしなくても必ずそのときの最大の数が取ってこれるということに気づいた
# alice_scoreとbob_scoreというように二つのスコアを準備しなくても一つの変数にそのときの最大数を足したあと、その変数から次の瞬間の最大数を引くことによって一つの変数でアリスとボブのスコアの差が計算できる
N=int(input())
A=list(map(int,input().split()))
list.sort(A,reverse=True)
ans = 0
for i in range(len(A)):
  if i%2==0:
    ans += A[i]
  else:
    ans -= A[i]

print(ans)