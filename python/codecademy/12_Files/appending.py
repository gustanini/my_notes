#Inside your with block, add “Air Buddy\n” to cool_dogs.txt
with open('cool_dogs.txt', "a") as cool_dogs_file:
  cool_dogs_file.write("Air Buddy\n")