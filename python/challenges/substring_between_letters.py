# Write your substring_between_letters function here:

# Uncomment these function calls to test your function:
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"

def substring_between_letters(word, x, y):
    start = word.find(x)
    end = word.find(y)
    if start == -1 or end == -1:
        return word
    else:
        return word[start+1:end]

print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))