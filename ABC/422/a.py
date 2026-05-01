# 私の回答
# 正解
i,bar,j = map(str,input())
i,j = int(i),int(j)
if j == 8:
    i += 1
    j = 1
else:
    j += 1
print(f"{i}-{j}")