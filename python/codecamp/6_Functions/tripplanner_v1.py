# welcome message function
def trip_planner_welcome(name):
  print(f"Welcome to tripplanner v1.0 {name}")

trip_planner_welcome("Rafael")

# time rounding function
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(50.55)
print(estimate)

# trip setup function
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print(f"Your trip starts off in {origin}")
  print(f"And you are traveling to {destination}")
  print(f"You will be traveling by {mode_of_transport}")
  print(f"It will take approximately {str(estimated_time)} hours")

# calling the final function
destination_setup('NY', 'NJ', estimate, 'plane')