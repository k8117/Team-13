import random  # Import the random module to simulate rolling dice

def roll_dice():
    """Roll two six-sided dice and return their face values."""
    # Generate random numbers between 1 and 6 for both dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def main():
    print("Welcome to the game of Craps!")  # Greet the user

    # Ask the user to type "roll" to start the game
    while True:
        command = input("Type 'roll' to roll the dice or 'unroll' to exit: ").lower()
        if command == 'roll':
            break
        elif command == 'unroll':
            print("Exiting the game. Goodbye!")
            return
        else:
            print("Invalid input. Please type 'roll' or 'unroll'.")

    # First roll of the dice
    die1, die2 = roll_dice()            # Roll the dice
    first_roll_sum = die1 + die2        # Calculate the sum of the dice
    print(f"You rolled {die1} + {die2} = {first_roll_sum}")  # Show the result

    # Check the result of the first roll
    if first_roll_sum in (7, 11):              # If the sum is 7 or 11, the player wins
        print("You win on the first roll!")
    elif first_roll_sum in (2, 3, 12):         # If the sum is 2, 3, or 12, the player loses
        print("Craps! You lose on the first roll.")
    else:
        # If it's not an immediate win or loss, set the "point" to this sum
        point = first_roll_sum
        print(f"Your point is {point}. Keep rolling to make your point.")  # Inform the user about their point

        while True:          # Keep rolling until the player wins or loses
            command = input("Type 'roll' to roll the dice or 'unroll' to exit: ").lower()
            if command == 'roll':
                die1, die2 = roll_dice()            # Roll the dice again
                roll_sum = die1 + die2              # Calculate the new sum
                print(f"You rolled {die1} + {die2} = {roll_sum}")  # Show the result

                # Check if the player makes their point or rolls a 7
                if roll_sum == point:          # If the sum matches the point, the player wins
                    print("You made your point! You win!")
                    break                      # Exit the loop, game over
                elif roll_sum == 7:            # If the sum is 7 before making the point, the player loses
                    print("You rolled a 7 before making your point. You lose.")
                    break                      # Exit the loop, game over
            elif command == 'unroll':
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid input. Please type 'roll' or 'unroll'.")

# Ensure the script runs when executed directly
if __name__ == "__main__":
    main()                 # Start the game
    

"""
 Output of this program:   
                        Welcome to the game of Craps!
                        Type 'roll' to roll the dice or 'unroll' to exit: roll
                        You rolled 2 + 4 = 6
                        Your point is 6. Keep rolling to make your point.
                        Type 'roll' to roll the dice or 'unroll' to exit: roll
                        You rolled 2 + 1 = 3
                        Type 'roll' to roll the dice or 'unroll' to exit: roll
                        You rolled 6 + 3 = 9
                        Type 'roll' to roll the dice or 'unroll' to exit: roll
                        You rolled 4 + 6 = 10
                        Type 'roll' to roll the dice or 'unroll' to exit: roll
                        You rolled 2 + 4 = 6
                       You made your point! You win!
"""
