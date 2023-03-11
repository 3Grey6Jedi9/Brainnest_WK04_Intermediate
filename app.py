import itertools
import math


def is_prime(number):
    if number == 1:
        return True
    else:
        for i in range(2,int(math.sqrt(number))+1):
            if number % i == 0:
                return False
            else:
                continue
        return True



def circular(number):
    number_str = str(number)
    rotations = []

    for i in range(len(number_str)):
        rotations.append(int(number_str))
        number_str = number_str[1:] + number_str[0]
    return rotations



def naturals_gen():
    n = 1
    while n < 1e6:
        yield n
        n += 1

naturals = naturals_gen()

count = 0

prime = ''
for n in naturals:
    c = circular(n)
    for p in c:
        if is_prime(p):
            continue
        else:
            prime = 0
    if prime != 0:
        count += 1
    prime = ''

print(count)








