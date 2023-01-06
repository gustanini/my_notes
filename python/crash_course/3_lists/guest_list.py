guests = ["Ramon", "Jose", "Carla"]

#for i in guests:
#    print(f'I invite you {i} to a dinner.')
    
removed = guests.pop()
#print(f'Unfortunately {removed.title()} is not coming to the dinner on Sunday.')
guests.append("Clara")

#for i in guests:
#    print(f'I invite you {i} to a dinner.')

guests.insert(0, "Carlos")
guests.insert(2, "Karen")
guests.append("Carlos")

for i in guests:
    print(f'I invite you {i} to a dinner.')

print("Due to a series of unfortunate events, only two will be able to come on Sunday")
removed = guests.pop()
print(f"Im deeply sorry {removed}")
removed = guests.pop()
print(f"Im deeply sorry {removed}")
removed = guests.pop()
print(f"Im deeply sorry {removed}")
removed = guests.pop()
print(f"Im deeply sorry {removed}")

for i in guests:
    print(f'{i} you are still invited.')

del guests[1]
del guests[0]

print(guests)