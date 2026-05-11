# 私の回答
# 不正解
# なんとかTと一致するような操作の回数などは出せそうだったが、最小回数を求めるやり方が思いつかなかった
N = int(input())
S = [input() for i in range(N)]
T = [input() for i in range(N)]
print(S)
print(T)

# 模範回答
# 美しい
# resultは考えられる最大操作回数であるN*Nに設定しておく
# 四回ループは0度、90度、180度、270度で試すため
# resultはより小さい値を見つけるたびに更新されていく
# i + sum(~)という書き方は90度回転にもコストがかかるため、回転数を足している
# sum(S[i][j] != T[i][j] for i in range(N) for j in range(N))というのはTとSで違う色で塗られている箇所がどれだけあるかの合計である
# この問題の場合は実際に塗る色を変更するということはしなくても違う色のマスの数だけ数えれば良い。
# グリッドに対してインデックスで[::-1]というように指定すると右に90度回転したグリッドが得られる
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

result = N * N
for i in range(4):
    result = min(result, i + sum(S[i][j] != T[i][j] for i in range(N) for j in range(N)))
    S = list(zip(*S[::-1]))

print(result)
