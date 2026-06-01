# 私の回答
# 正解
A,B,C = map(int,input().split())
if (A == B == C) or (A+B == C) or (A+C == B) or (B+C == A):
    print("Yes")
else:
    print("No")