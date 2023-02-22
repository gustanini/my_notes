# weight = 41.5
weight = float(input("Article weight in pounds:\n"))

# ground shipping

if weight <= 2:
  price = (weight * 1.50 + 20)
elif weight <= 6 and weight >=2:
  price = (weight * 3 + 20)
elif weight <= 10 and weight >=6:
  price = (weight * 4 + 20)
else:
  price = (weight * 4.75 + 20)

print(f"Ground shipping costs: {price} USD\n")

# premium

premium_price = 125

print(f"Premium shipping costs: {premium_price} USD\n")

# drone

drone_price = 0

if weight <= 2:
  drone_price = (weight * 1.50*3)
elif weight <= 6:
  drone_price = (weight * 3*3)
elif weight <= 10:
  drone_price = (weight * 4*3)
else:
  drone_price = (weight * 4.75*3)
print(f"Drone shipping costs: {drone_price} USD\n")