#Write your function here

def more_frequent_item(lst, num1, num2):
    if lst.count(num1) >= lst.count(num2):
        return num1
    else:
        return num2

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))