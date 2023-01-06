#method 1 with list
top_3 = ["Rome","Venice","Italy"]

def top_tourist_locations_italy(city):
  first = city[0]
  second = city[1]
  third = city[2]
  #return these values
  return first, second, third


most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy(top_3)

print(most_popular1)
print(most_popular2)
print(most_popular3)

# method 2 defining inside the function
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  #return these values
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)