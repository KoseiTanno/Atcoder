# 私の回答
# 正解
# 文字列と数値型を変換して桁の数字を扱う工夫をした
a1,a2 = map(int,input().split())
num_lst = [a1,a2]

def reverse(a,b):
    lst = []
    c = str(int(a)+int(b))
    for i in c:
        lst.insert(0,i)
    return "".join(lst)

for i in range(2,10):
    num_lst.append(reverse(num_lst[i-2],num_lst[i-1]))
print(num_lst[-1])
