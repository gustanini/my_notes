#Write your function here

def append_sum(lst):
    count = 0
    while count < 3:
        lst.append(lst[-1] + lst[-2])
        count += 1
    return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))