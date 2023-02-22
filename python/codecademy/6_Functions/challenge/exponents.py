def exponents(bases, powers):
    lst2 = []
    for base in bases:
        for power in powers:
            lst2.append(base ** power)
    return lst2