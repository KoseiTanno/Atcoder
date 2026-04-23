# 私の回答
# 簡単にできるかと思ったらdreamerとeraserがつながってdreameraserとなったときの判定式が難しかった
# 正解出来なかった
# S = input()
# T = ""
# for i in ["dreamer","dream","eraser","erase"]:
#     if i in S:
#         T += i
# if sorted(T) in sorted(S):
#     print("YES")
# else:
#     print("NO")

# 模範回答
S = input()
S = S.replace("eraser","")
S = S.replace("erase","")
S = S.replace("dreamer","")
S = S.replace("dream","")

print("YES" if S == "" else "NO")