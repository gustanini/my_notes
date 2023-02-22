# Write a function called poem_title_card that takes two inputs: the first input should be title and the second poet. The function should use .format() to return a certain string

def poem_title_card(title, poet):
  return 'The poem "{}" is written by {}.'.format(title,poet)

poem_title_card("I Hear America Singing", "Walt Whitman")

print(poem_title_card("I Hear America Singing", "Walt Whitman"))