# Notes: I didn't include proper error handling in this file to make it easier to read; if we get far enough into the
# lesson, I might add it in.

import sys, time, random

moveList = ["rock", "paper", "scissors"]


def tripleDotDicePrint():
    for i in range(3):
        sys.stdout.flush()
        time.sleep(0.67)
        sys.stdout.write(".")


def makeComputerMove():
    return moveList[random.randint(0, 2)]


def determineWinner(userMove, compMove):
    if userMove == compMove:
        return "It's a tie!"
    elif userMove == "rock":
        if compMove == "scissors":
            return "You win!"
        else:
            return "You lose!"
    elif userMove == "paper":
        if compMove == "rock":
            return "You win!"
        else:
            return "You lose!"
    else:
        if compMove == "paper":
            return "You win!"
        else:
            return "You lose!"

while True:
    userTurn = str(input(("*" * 32) + "\nWelcome to Rock, Paper Scissors! \n"
                         "Would you like to choose 'rock', 'paper' or 'scissors'? Type your desired move: ")).lower()

    while not moveList.__contains__(userTurn):
        print("Invalid move, please try again.")
        userTurn = str(input("Would you like to choose 'rock', 'paper' or 'scissors'? Type your desired move: "))

    print("You have selected " + userTurn + ". It's the computer turn. \nThe computer is choosing ")

    tripleDotDicePrint()

    compTurn = makeComputerMove()

    print("\nThe computer has chosen " + compTurn + ".")

    time.sleep(1)

    print(determineWinner(userTurn, compTurn))

    playAgain = input("Would you like to play again? Enter 'yes' for yes, otherwise enter 'no'. ")

    while not (playAgain == "yes" or playAgain == "no"):
        print("Invalid input, please try again.")
        playAgain = input("Would you like to play again? Enter 'yes' for yes, otherwise enter 'no'. ")

    if playAgain == "no":
        exit()