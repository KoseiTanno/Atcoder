# https://atcoder.jp/contests/abc380/tasks/abc380_a
# 私の回答
# 正解

N = list(input())
is_one_one = N.count("1") == 1
is_two_two = N.count("2") == 2
is_three_three = N.count("3") == 3

print("Yes" if is_one_one and is_two_two and is_three_three else "No")
