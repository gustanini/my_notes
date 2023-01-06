def reversed_list(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] != lst2[(len(lst2)-1 - i)]:
            return False
            break
    return True