from collections import deque

N = int(input())
S = input()

res = deque([1])
front = True

for i in range(1,N):
    v = i + 1
    # 次の数字を列の一番後ろに置きたいが、今は右左どちらが一番後ろかを判断して、一番後ろに挿入する。
    if S[i] == "o":
        if front:
            res.append(v)
        else:
            res.appendleft(v)
        front = not front
    else:
        if front:
            res.append(v)
        else:
            res.appendleft(v)
# 今がどちらの向きかを認識して出力
print(*res if front else reversed(res))