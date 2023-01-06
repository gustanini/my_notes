inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory) # get n of items
print(inventory_len)

first = inventory[0] # select first item
print(first)

last = inventory[-1] # select last item
print(last)

inventory_2_6 = inventory[2:6] # select items starting from 2 ending in 6 not inclusive
print(inventory_2_6)

first_3 = inventory[:3] # select first three items

twin_beds = inventory.count('twin bed') # count item

removed_item = inventory.pop(4) #remove 5th item

inventory.insert(10, "19th Century Bed Frame") # insert new item on 11th place

print(sorted(inventory)) # sort without changing list
print(inventory)

inventory.sort() # sort changing list
print(inventory)