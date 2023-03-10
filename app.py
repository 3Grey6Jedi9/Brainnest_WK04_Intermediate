coins = [2, 1, 0.5, 0.2 ,0.1, 0.05, 0.02, 0.01]

count = 0

def natural_numbers(maxfac):
    n = 1
    while n <= maxfac:
        yield n
        n += 1

maxfac = int (max(coins) / min(coins))

naturals = natural_numbers(maxfac)

for c in coins:
    if int(2 % c) == 0:
        count += 1
coins.remove(2)

for c in coins:
    for d in coins[coins.index(c)+1:]:
        for n in naturals:
            if c + d*n == 2:
                count += 1
                break
            else:
                continue



print(count)
