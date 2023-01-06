#Write your function here

def double_index(lst, index):
    if index <= len(lst):
        new_list = lst[:(index)]
        new_list.append(lst[index]*2)
        new_list + lst[index + 1:]
        return new_list
    else:
        return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))