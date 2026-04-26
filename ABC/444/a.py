# 私の回答
# 正解
# N = input()
# a = N[0]
# ok = True
# for i in N:
#     if i != a:
#         ok = False
# print("Yes" if ok else "No")

# 模範回答
# 今回の問題の場合は三桁って決まっているからこれでも良かった
N = input()

if N[0] == N[1] == N[2]:
  print("Yes")
else:
  print("No")