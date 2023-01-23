heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

# list with people taller than 161
can_ride_coaster = [i for i in heights if i > 161]

print(can_ride_coaster)