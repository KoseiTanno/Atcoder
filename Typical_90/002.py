# 私の回答
# 解法が皆目見当もつかない
# N = int(input())

# 公式の解説を踏まえた私の回答
# 正解だがTLE
# N = int(input())
# if N % 2 == 1:
#     exit()
# result = []

# def is_ok(kakko):
#     L = len(kakko)
#     cnt_left = 0
#     cnt_right = 0
#     for i in range(L):
#         if kakko[i] == "(":
#             cnt_left += 1
#         else:
#             cnt_right += 1
#         if cnt_left < cnt_right:
#             return False
#     if (cnt_left == cnt_right) and L == N:
#         return True
#     return False

# for i in range(2**N-1):
#     bit = f"{i:b}"
#     M = len(bit)
#     lst = [0] * M
#     for j in range(M):
#         if bit[j] == "0":
#             lst[j] = ")"
#         else:
#             lst[j] = "("
#     if is_ok(lst):
#         result.append(lst)
# for i in reversed(result):
#     print("".join(i))

# 模範回答
# 再帰関数
# 奇数の時は空リストをreturnして、2の時は()をreturn
# それ以外の時は()に()をどう挿入していくかということを考える
# N = int(input())
# def gen(N):
#     if N % 2 == 1:
#         return []
#     elif N == 2:
#         return ["()"]
#     else:
#         re = []
#         for x in gen(N - 2):
#             re += [x[:i] + "()" + x[i:] for i in range(len(x))]
#         return sorted(list(set(re)))

# print("\n".join(gen(N)))

# 模範回答を踏まえた私の回答
# 正解
# 再帰関数便利だな
N = int(input())
def gen(N):
    if N % 2 != 0:
        exit()
    elif N == 2:
        return ["()"]
    else:
        res = []
        for x in gen(N-2):
            res += [x[:i] + "()" + x[i:] for i in range(N)]
        return sorted(list(set(res)))
print("\n".join(gen(N)))
