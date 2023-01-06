# Your code below:
toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2,6,1,3,2,7,2]

pizza_and_prices = [[2, "pepperoni"],[6, "pineapple"],[1, "cheese"],[3, "sausage"],[2, "olives"],[7, "anchovies"],[2, "mushrooms"]]
#2D list
num_two_dollar_slices = prices.count(2) #count 2 dollar slices
num_pizzas = len(toppings) #count total slices

print(f"We sell {num_pizzas} different kinds of pizza!") #announcement

print(pizza_and_prices) #print unsorted list

cheapest_pizza = pizza_and_prices[0][0]
priciest_pizza = pizza_and_prices[-1][-1]#selected cheapest and most expensive

pizza_and_prices.remove(pizza_and_prices[-1]) # remove most expensive
pizza_and_prices.insert(4, [2.5, "peppers"]) # add new pizza

pizza_and_prices.sort() #sort by price

print(pizza_and_prices) #checking sorted and modified list

three_cheapest = pizza_and_prices[:3] #selected 3 cheapest slices

print(three_cheapest)