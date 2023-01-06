#convert f to degrees celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

#do the opposite
def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

####

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#calculate force
def get_force(mass, acceleration):
  return mass * acceleration

#set a variable using the function then print it
train_force = get_force(train_mass, train_acceleration)
print(train_force)

print(f"The GE train supplies {train_force} Newtons of force.")

#calculate energy
def get_energy(mass, c = 3*10**8):
  return mass * c**2

#set a variable using the function then print it
bomb_energy = get_energy(bomb_mass)
print(f'A 1kg bomb supplies {bomb_energy} Joules.')

#calculate work (this function needs to call get_force for the calculations)
def get_work(mass, acceleration, distance):
  #call get_force using mass and accel to calculate force
  force = get_force(mass, acceleration)
  work = force * distance
  return work

#set a variable using the function then print it
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")