#Print out the contents of logger.csv by calling .read() on the file. Notice that it is parsed as a string.

with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())