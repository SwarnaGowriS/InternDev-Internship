import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        input("Press Enter to roll the dice (or type 'exit' to quit): ")
        dice_value = roll_dice()
        print(f"You rolled a {dice_value}!")
        
        # Ask the user if they want to roll again
        roll_again = input("Do you want to roll the dice again? (yes/no): ").strip().lower()
        
        if roll_again == 'yes':
            # If the user wants to roll again, continue the loop
            continue
        else:
            # If the user types anything other than 'yes', end the game
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
