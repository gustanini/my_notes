def same_values(lst1, lst2):
    lst3 = []
    for i in range(0, len(lst1)):
        if lst1[i] == lst2[i]:
            lst3.append(lst1[i])
        else:
            continue
    return lst3