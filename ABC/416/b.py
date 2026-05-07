# 私の回答
# 不正解
# 時間をかければ解けそうだったが、上手い解法は思いつかなそうだった
# S = input()
# N = len(S)
# T = "o" * N
# print(T)
# for i in range(N):
#     if S[i] == "#":
#         T = T[:i] + "#" + T[i+1:]
# print(T)
# for i in range(N):
#     for j in range(i,N-2):
#         print(T[i:j+3])
#         s = T[i:j+3]
#         if s[0] & s

# 模範回答
# #でサンドするときにまず最初の#でまだoを入れてないよというフラグを作り、Tにoを追加したらフラグをtrueに切り替える。
# #がない場合はoが一度だけ追加されて終わる。
# ループをN回回しているのでSの要素数以上の文字列ができることもない
S = input()
N = len(S)
T = []

f = False

for i in range(N):
    if S[i]=='#':
        T.append('#')
        f = False
    elif f == False:
        T.append('o')
        f = True
    else:
        T.append('.')

print(''.join(T))