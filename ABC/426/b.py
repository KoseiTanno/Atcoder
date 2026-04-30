# 私の回答
# 正解
# 辞書型を使ってみた
# for文でkeyとvalueをin items()で回すのが便利
from collections import Counter
strings = Counter(input())
for key,value in strings.items():
    if value == 1:
        print(key)
        exit()