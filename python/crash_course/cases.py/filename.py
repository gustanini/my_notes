file = "/home/user/downloads/notes.txt"
file = file.removesuffix('.txt')
file = file.removeprefix('/home/user/downloads/')
print(file)