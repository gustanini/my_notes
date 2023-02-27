# Write your every_other_letter function here:

# Uncomment these function calls to test your function:
#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print 

def every_other_letter(my_string):
    string = ''
    for i in range(0, len(my_string), 2):
        string += my_string[i]
    return string



print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 