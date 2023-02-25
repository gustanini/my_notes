import csv

#Create a list called isbn_list, iterate through books_reader to get the ISBN number of every book in the CSV file. Use the ['ISBN'] key for the dictionary objects passed to it.

with open('books.csv', newline='') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [row['ISBN'] for row in books_reader]