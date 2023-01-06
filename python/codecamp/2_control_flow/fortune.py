import random

name = input("Hello, I am the fortune teller, what is your name?:\n")
question = input("Your question:\n")
answer = ""


random_number = random.randint(1,9) #generates random number
#print(random_number) tests

#reads random number

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
else:
    print("Error")

# Output

if name == "" and question != "":
    print(f"Your question: '{question}'\n") # no name with question
else:
    print(f"{name.title()} asks: '{question}'\n") # name with question

# Final Answer

if question == "":
    print("Ask and thou shall receive.")
else:
    print(f"Fortune teller's answer: '{answer}'")