S = input()
N = len(S)
lst = []
i = 0
cnt = 0
while "".join(lst) != S:
    cnt += 1
    if S[i] == "0" and i+1 <= N-1:
        if S[i] == S[i+1] == "0":
            lst.append("00")
            i += 2
            continue
    lst.append(S[i])
    i += 1
print(cnt)