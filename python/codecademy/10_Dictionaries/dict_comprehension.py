drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

#create a variable called zipped_drinks that is an iterator of pairs between the drinks list and the caffeine list

zipped_drinks = zip(drinks, caffeine)

#Create a dictionary by using a dict comprehension

drinks_to_caffeine = {key:value for key, value in zipped_drinks}