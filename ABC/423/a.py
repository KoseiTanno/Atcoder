# 私の回答
# 正解
# 今回の問題では1000区切りということだったが保守性の観点からその値が変わってもいいようにした
# X,C = map(int,input().split())
# segment = 1000
# fee = 0
# withdraw = 0
# while(fee + withdraw <= X):
#     withdraw += segment
#     fee += C
# print(withdraw-segment)

# 模範回答
# 切り捨てた商に1000かければ良かった
X, C = map(int, input().split())
print(X // (1000 + C) * 1000)

