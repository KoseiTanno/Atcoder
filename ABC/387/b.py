# 私の回答
# 正解
X = int(input())
total = 0
for i in range(10):
    for j in range(10):
        masu = i * j
        if X != masu:
            total += masu
print(total)