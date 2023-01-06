favorite_language = 'python '
print(favorite_language) # will print with whitespace

favorite_language = 'python '
print(favorite_language.rstrip()) # will remove right whitespace

favorite_language = 'python '
favorite_language = favorite_language.rstrip() # saving variable removing right whitespace
print(favorite_language)

favorite_language = ' python '
favorite_language = favorite_language.rstrip() # remove right whitespace
favorite_language = favorite_language.lstrip() # remove left whitespace
favorite_language = favorite_language.strip() # remove all whitespace
print(favorite_language)