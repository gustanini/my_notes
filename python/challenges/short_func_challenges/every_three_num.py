#Write your function here

def every_three_nums(num):
    lst = range(num, 101, 3)
    if num > 100:
        return []
    else:
        return list(lst)

#Uncomment the line below when your function is done
print(every_three_nums(91))