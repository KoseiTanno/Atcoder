N = int(input())
say = list(map(int,input().split()))
real = list(map(int,input().split()))

for i in range(N):
    if i+1 != real[say[i]-1]:
        print("No")
        exit()
print("Yes")