# 私の回答
# 正解
S,A,B,X = map(int,input().split())
quo = X//(A+B)
rem = X % (A+B)
result = S*quo*A
if rem > A:
    result += S*A
    print(result)
else:
    result += rem*S
    print(result)
