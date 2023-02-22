def odd_indices(lst):
    lst2 = []
    for index in range(1, len(lst), 2):
      lst2.append(lst[index])
    return lst2 

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))