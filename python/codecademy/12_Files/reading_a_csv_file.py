import csv

#Using csv.DictReader read the contents of cool_csv_file into a new variable

with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  #For each row in cool_csv_dict print out that row’s "Cool Fact".
  for row in cool_csv_dict:
    print(row["Cool Fact"])
