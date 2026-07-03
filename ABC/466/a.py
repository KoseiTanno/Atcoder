N = int(input())
X = list(map(int,input().split()))
allminus = True
for i in X:
    if i >= 0:
        allminus = False
if allminus:
    print("Yes")
else:
    print("No")