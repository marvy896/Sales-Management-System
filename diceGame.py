def roll_dice():
    import random
    return random.randint(1, 6)

Name = input("Enter your name: ")
print(f"Hello, {Name}! Welcome to my Dice Game!")
def PlayGame():
    print("Do you want to play? (y/n)")
    while True:
        choice = input().lower()
        if choice == "y":
            print("Great! Let's start the game.")
            while True:
                    input("Press Enter to roll the dice...")
                    result = roll_dice()
                    print(f"You rolled a {result}!")
                    if result == 6:
                        print("Congratulations! You rolled a 6! \n Do you want to play again? (y/n)")
                        break
                    else:
                        print("Try again!")
        elif choice == "n":
            print("Okay, maybe next time. Goodbye!")
            break        
        else:
         print("Invalid input. Please enter 'y' or 'n'.")
         
PlayGame()

