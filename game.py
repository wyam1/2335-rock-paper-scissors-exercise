# game.py

print("Rock, Paper, Scissors, Shoot!\n")


testing1 = "<< That's a solid choice!!"
user_input = input("Enter Rock, Paper, or Scissors: ")
print("User Choose: ", user_input, testing1)

# validate the user input below

if (user_input == "rock") or (user_input == "Paper") or (user_input == "Scissors"):
# if user_input == "rock":
    print("Valid Choice")
else:
    print("nah, choose something else homie")
    quit()