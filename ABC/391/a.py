# 私の回答
# 正解
D = input()
N = len(D)
my_dict = {"N":"S","S":"N","E":"W","W":"E"}        
if N == 1:
    print(my_dict[D])
else:
    lst = []
    for i in range(N):
        lst.append(my_dict[D[i]])
    print("".join(lst))