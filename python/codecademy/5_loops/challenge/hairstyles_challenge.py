hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#find average cost of all haircuts
total_price = 0

for x in prices:
  total_price += x
average_price = total_price / len(prices)
print(f"Average Haircut Price: {average_price}")

#lower the price off all haircuts into a list
new_prices = [price - 5 for price in prices]
print(new_prices)

#calculate total revenue adding the product of all prices and number of purchases
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
  i += 1

print(f"Total Revenue: {total_revenue}")

#find average total revenue
average_daily_revenue = total_revenue / 7
print(f"Daily Average Revenue: {average_daily_revenue}")

#create a comprehension list using all cuts under 30 and print it as an ad
all_cuts = 0
all_cuts = [[hairstyles[i], new_prices[i]] for i in range(len(hairstyles)) if new_prices[i] < 30]

print(f"Cuts Under 30$: {all_cuts}")