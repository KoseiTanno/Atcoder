S = input()
buttons = ["00","0","1","2","3","4","5","6","7","8","9"]
while S != "":
    lst = []
    saidai = 1
    for i in buttons:
        if i in S:
            saidai = max(saidai,len(i))
            lst.append(i)
    if saidai == 2:
        S.remove("00")

    