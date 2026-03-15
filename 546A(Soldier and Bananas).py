price, wallet, bananas = map(int, input().split())
balance = wallet
for x in range(1, bananas+1):
    balance -= price * x

print(max(-balance, 0))
