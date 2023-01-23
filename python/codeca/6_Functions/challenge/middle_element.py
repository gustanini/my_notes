def middle_element(lst):
    if len(lst) % 2 != 0:
        return lst[int(len(lst)/2)]
    else:
        return ((lst[int(len(lst)/2)] + lst[int((len(lst)-1)/2)]) / 2)

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))