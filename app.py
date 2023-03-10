naturals_9 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

unusual = set()

def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1

naturals = natural_numbers()

def descomposed(number):
    # Descompose the numer like 123 1, 2 and 3

# So maximum 4 figures and minimum 1 figure

# I start checlking all nmbers if the producnt is ok I descompose the number and I put them into a set that set must bu equel
# to naturals9
