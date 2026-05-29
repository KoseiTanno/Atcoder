S = input()
buttons = ["0","1","2","3","4","5","6","7","8","9"]
zz = "00"
while S != "":
    lst = []
    if zz in S:
        S.remove(zz)
    for i in buttons:
        if