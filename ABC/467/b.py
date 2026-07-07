N = int(input())
money = 10000
keeper = 10000
for i in range(N):
    price,pay,S = input().split()
    price = int(price)
    pay = int(pay)
    exchange = pay-price
    if S == "keep":
        money -= pay
    else:
        money -= price
    keeper -= price
print(keeper-money)