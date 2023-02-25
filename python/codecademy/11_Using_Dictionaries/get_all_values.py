num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

#add each value to the total_exercises variable

for values in num_exercises.values():
  total_exercises += values

print(total_exercises)