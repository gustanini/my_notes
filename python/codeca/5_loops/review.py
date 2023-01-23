# Your code below:
single_digits = range(0,10)
single_digits = list(single_digits)
squares = []
cubes = []

for digit in single_digits:
  squares.append(digit ** 2)
  cubes.append(digit ** 3)
print(single_digits)
print(squares)
print(cubes)