#pointing to the file just_the_first.txt. Store that file object in the variable first_line_doc.

with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
print(first_line)