import math

cool_numbers = set()
def natural_gen():
    n = 3
    while n < 2177280:
        yield n
        n += 1

naturals = natural_gen()

def descom(number):
    s = str(number)
    d = []
    for i in s:
        d.append(int(i))
    return d

for n in naturals:
    d = descom(n)
    f = []
    for i in d:
        f.append(math.factorial(i))
    if n == sum(f):
        cool_numbers.add(n)



print(cool_numbers)


