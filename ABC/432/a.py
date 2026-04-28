# 私の回答
# 正解
A,B,C = map(int,input().split())
lst = sorted([A,B,C],reverse=True)
lst = [str(i) for i in lst]
print("".join(lst))