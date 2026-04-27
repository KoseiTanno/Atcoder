# 私の回答
# 正解
# 1時間ぐらいかかってしまった
N = list(map(int,str(input())))
sq_sm_lst = []
while(1):
    for i in range(len(N)):
        N[i] = N[i] **2
    if sum(N) == 1:
        print("Yes")
        exit()
    elif sum(N) in sq_sm_lst:
        print("No")
        exit()
    sq_sm_lst.append(sum(N))
    N = list(map(int,str(sum(N))))
