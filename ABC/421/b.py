a1,a2 = map(int,input().split())
a3 = str(a2+a1)

def reverse(a,b):
    lst = []
    c = str(a+b)
    for i in c:
        lst.insert(0,i)
    return "".join(lst)

for i in range(1,10):
    print(reverse(a1,a2))
