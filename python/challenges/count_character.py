# Write your count_char_x function here:

# Uncomment these function calls to test your tip function:
#print(count_char_x("mississippi", "s"))
# should print 4
#print(count_char_x("mississippi", "m"))
# should print 1

def count_char_x(word, x):
  count = 0
  for letter in word:
    if x in letter:
      count += 1
  return count

print(count_char_x("mississippi", "s"))