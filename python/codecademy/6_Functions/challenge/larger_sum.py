def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for i in lst1:
        sum1 += i
    for i in lst2:
        sum2 += i
    if sum1 >= sum2:
        return lst1
    else:
        return lst2