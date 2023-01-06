sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

#determine the number of scoops sold
scoops_sold = 0

for location in sales_data:
  print(location)
  #add each scoop sold into scoops sold var
  for scoop in location:
    scoops_sold += scoop

print(scoops_sold)