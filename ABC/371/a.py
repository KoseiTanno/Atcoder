# https://atcoder.jp/contests/abc371/tasks/abc371_a
# 私の回答
# 正解

lst = input().split()
if lst == ["<","<","<"] or lst == [">",">",">"]:
    print("B")
elif lst == ["<","<",">"] or lst == [">",">","<"]:
    print("C")
elif lst == [">","<","<"] or lst == ["<",">",">"]:
    print("A")
