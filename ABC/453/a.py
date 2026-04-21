# 私の回答
# N = int(input())
# S = list(input())
# for i in range(N):
#     if S[0] == "o":
#         del S[0]
# print("".join(S))

# 模範解答
# lstrip()は文字列の先頭から指定した文字を削除するメソッド
# 例えば、"oooabc".lstrip("o")は"abc"を返す。
# なお、複数の文字を指定した場合は、いずれかの文字が先頭にある限り削除される。
N = int(input())
S = input()
print(S.lstrip("o"))