authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# create a list called author_names containing each individual author name as it’s own string.

author_names = authors.split(',')
print(author_names)

author_last_names = []

# Create another list called author_last_names that only contains the last names of the poets in the provided string.

for name in author_names:
  author_last_names.append(name.split()[-1])

print(author_last_names)