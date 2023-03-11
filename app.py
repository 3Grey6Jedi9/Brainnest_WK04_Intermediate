from fractions import Fraction
import itertools


curious = {str(Fraction(49,98))}


def tupint(tup):
    l1 = list(tup)[0]
    l2 = list(tup)[1]
    n = int(''.join([str(l1), str(l2)]))
    return n


def small(aa):
    for aa in aa:
        aa = int(aa)
    return aa


# Generate all permutations of two digits from 0 to 9, including duplicates
for a in itertools.product(range(1,10), repeat=2):
    for b in itertools.product(range(10), repeat=2):
        if set(a) & set(b) != 0:
            aa = set(a) - set(b)
            bb = set(b) - set(a)
            if aa != set() and bb != set():
                try:
                    if tupint(a)/tupint(b) == small(aa)/small(bb):
                        fr = tupint(a)/tupint(b)
                        if fr < 1:
                            curious.add(str(Fraction(tupint(a), tupint(b))))
                        else:
                            continue
                    else:
                        continue
                except ZeroDivisionError:
                    continue
            else:
                continue
        else:
            continue

print(curious)



