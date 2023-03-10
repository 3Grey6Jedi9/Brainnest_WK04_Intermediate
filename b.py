coins = [2, 1, 0.5, 0.2 ,0.1, 0.05, 0.02, 0.01]



for c in coins:
    print(c)
    for d in coins[coins.index(c)+1:]:
        print(d)
        break
