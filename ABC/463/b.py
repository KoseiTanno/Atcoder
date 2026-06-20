N,X = input().split()
N = int(N)
my_dict = {"A":0,"B":1,"C":2,"D":3,"E":4}
for i in range(N):
    S = input()
    if S[my_dict[X]] == "o":
        print("Yes")
        exit()
print("No")
        
