current_budget = 3500.75
shirt_expense = 9
def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 

# We need to add a tshirt expense
def deduct_expense(budget, expense):
  return budget - expense

# define budget after expense
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)