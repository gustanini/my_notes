love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

# First, use .strip() on each line in the list to remove the unnecessary whitespace and save it as a new list

love_maybe_lines_stripped = []

for name in love_maybe_lines:
  love_maybe_lines_stripped.append(name.strip())

print(love_maybe_lines_stripped)

# .join() the lines in love_maybe_lines_stripped together into one large multi-line string, love_maybe_full, that can be printed to display the poem.

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)