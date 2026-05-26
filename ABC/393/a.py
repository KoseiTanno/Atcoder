# 私の回答
# 正解
S = list(map(str,input().split()))
if S[0] == "fine" and S[1] == "fine":
    print(4)
elif S[0] == "sick" and S[1] == "fine":
    print(2)
elif S[0] == "fine" and S[1] == "sick":
    print(3)
elif S[0] == "sick" and S[1] == "sick":
    print(1)