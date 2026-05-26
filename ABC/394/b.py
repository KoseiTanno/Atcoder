# 私の回答
# 正解
# 二つのリストを辞書にする方法
# 辞書を特定のkeyでソートする方法
N = int(input())
moji = [input() for _ in range(N)]
kazu = [len(moji[i]) for i in range(N)]
my_dict = {key: val for key,val in zip(moji,kazu)}
my_dict = dict(sorted(my_dict.items(),key=lambda x: x[1]))
print("".join(my_dict.keys()))