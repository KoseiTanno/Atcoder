# 私の回答
# 正解
S = input()
N = len(S)
i = 0
lst = []
while("#" in S):
    if S[i] == "#":
        lst.append(i+1)
        S = S[:i] + "." + S[i+1:]
    i += 1
for j in range(0,len(lst)-1,2):
    print(f"{lst[j]},{lst[j+1]}")
