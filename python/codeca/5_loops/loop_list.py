students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

# adding two lists with + sign
students_plus = students_period_A + students_period_B
print(students_plus)

# adding two lists with a while loop
index = 0
length = 4
students = []
while index < length:
  students.append(students_period_A[index])
  students.append(students_period_B[index])
  index += 1

print(students)