# 私の回答
# 正解
# スライスをうまく使えるようになってきた
# count関数もうまく使えるようになってきた
# 問題文の数式をプログラムに落とし込めるようになってきた
S = input()
N = len(S)
rate = 0
if S.count("t") < 3:
    print(0)
    exit()
for i in range(N-2):
    for j in range(i+2,N):
        s = S[i:j+1]
        c = s.count("t")
        if (s[0] == s[-1] == "t") & (c >= 3):
            tmp_rate = (c-2)/(len(s)-2)
            if rate < tmp_rate:
                rate = tmp_rate
print(rate)