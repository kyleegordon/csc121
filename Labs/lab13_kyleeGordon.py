# Kylee Gordon Lab-13 03/23/2022

# This program is a random number guessing game.
# It generates a random number between 1 and 100
# then allows the user to guess what it is.
# It tells the user if their guess was too high or too low,
# and allows then to guess again. If the user guesses incorrectly
# 7 times, they lose the game. The program will keep track of the
# number of wins/losses for the user and the computer.
# The program will continue to run until told to stop by the user.

import random

# Global Variables
userWins = 0
computerWins = 0
incorrectGuesses = 0


def main():
    keep_playing = "yes"
    # Input/Processing
    while keep_playing != "x":
        play_game()
        keep_playing = input("\nEnter the letter 'x' to exit the game or any other key to continue: ")

    # Output
    print_results()


# This function generates a random number and allows the user to guess what it is
def play_game():
    global userWins, computerWins, incorrectGuesses
    incorrectGuesses = 0
    random_num = random.randint(1, 101)
    is_correct = False
    while not is_correct:
        if incorrectGuesses >= 7:
            print("Too many incorrect guesses, you lose!")
            computerWins += 1
            return
        user_guess = int(input("Guess a number between 1 and 100: "))
        is_correct = check_guess(user_guess, random_num)


# This function checks if the user's guess matches the random number
def check_guess(guess, number):
    global userWins, incorrectGuesses
    if guess > number:
        print("Too high, try again\n")
        incorrectGuesses += 1
        return False
    elif guess < number:
        print("Too low, try again\n")
        incorrectGuesses += 1
        return False
    else:
        print("You win!")
        userWins += 1
        return True


# This function prints the game results
def print_results():
    global userWins, computerWins
    print("\nThank you for playing, the results are: \n")
    print("User Wins: " + str(userWins) + "\nUser Losses: " + str(computerWins))
    print("\nComputer Wins: " + str(computerWins) + "\nComputer Losses: " + str(userWins))


main()
