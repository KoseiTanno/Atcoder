# 私の回答
# 正解
my_dict = {"Ocelot":1,"Serval":2,"Lynx":3}
X,Y= map(str,input().split())
if my_dict[X] >= my_dict[Y]:
    print("Yes")
else:
    print("No")
