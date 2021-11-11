#**********************  LeeAndrewC_CSCI1470_Prog8  *********************
#
# Name: Andrew Lee
#
# Course: CSCI 1470.01
#
# Assignment: Program #8
#
# Algorithm(or a brief purpose of the assignment):
#   Declare two identical decks of cards each with 13 cards (4 lists in total, two for each deck)
#       -- would've used dicts instead if we were being given style points :)
#   Ask the player if they want fast mode (fast mode displays less telemetry and instantly runs through all 13 rounds.
#       Slow mode displays more telemetry each round and waits for user input before moving on to the next round)
#   For 13 rounds:
#       Draw one random card from each deck
#       Give a point to whichever player drew the higher card (or no pts if it's a tie)
#       Remove each drawn card from its respective list so it can't be used again by that player
#   Compare player scores, declare a winner or a tie
#   Ask the player if they want to play again
#
#**********************************************************
import random


playAgain = "y"
gamesPlayed = 0
player1GamesWon = 0
player2GamesWon = 0
while playAgain == "y":

    rounds = 1

    deckName1 = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
    deckValue1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    deckName2 = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
    deckValue2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    player1score = 0
    player2score = 0

    fastMode = input("Play on fast mode? (y/n) ")

    while rounds <= 13:

        player1 = random.randint(0, len(deckValue1) - 1)
        player2 = random.randint(0, len(deckValue2) - 1)
        if fastMode == "n":
            print("PLAYER 1 ---------")
            print("ID {}".format(player1))
            print("Player 1 deck @ {} is {}".format(player1, deckValue1[player1]))
        print("Player 1 drew a {}.".format(deckName1[player1]))

        if fastMode == "n":
            print("PLAYER 2 ---------")
            print("ID {}".format(player2))
            print("Player 2 deck @ {} is {}".format(player2, deckValue2[player2]))
        print("Player 2 drew a {}.".format(deckName2[player2]))
        print()

        if deckValue1[player1] > deckValue2[player2]:
            player1score += 1
            if fastMode == "n":
                print("/----------------------------\\")
                print("|        Player 1 wins.      |")
                print("\----------------------------/")
            else:
                print("Player 1 wins.")
        elif deckValue2[player2] > deckValue1[player1]:
            player2score += 1
            if fastMode == "n":
                print("/----------------------------\\")
                print("|        Player 2 wins.      |")
                print("\----------------------------/")
            else:
                print("Player 2 wins")
        else:
            if fastMode == "n":
                print("/----------------------------\\")
                print("|        It was a Tie.       |")
                print("\----------------------------/")
            else:
                print("It was a Tie")

        print("Player 1 has {one} pts. \nPlayer 2 has {two} pts.".format(one=player1score, two=player2score))
        print("------------------------------------------------")

        deckValue1.pop(player1)
        deckName1.pop(player1)
        deckValue2.pop(player2)
        deckName2.pop(player2)
        # print(deckName1)
        # print(deckValue1)
        # print(deckName2)
        # print(deckValue2)
        rounds += 1
        if fastMode == "n":
            input("Enter any input to continue to next round")

    print()
    if player1score > player2score:
        print("/--------------------------------\\")
        print("|  Player 1 won with {} points!   |".format(player1score))
        print("\--------------------------------/")
        # print("Player 1 won with {} points!".format(player1score))
        player1GamesWon += 1
    elif player2score > player1score:
        print("/--------------------------------\\")
        print("|  Player 2 won with {} points!   |".format(player2score))
        print("\--------------------------------/")
        player2GamesWon += 1
        # print("Player 2 won with {} points!".format(player2score))
    else:
        print("/---------------------------------------------------\\")
        print("|  Player 1 and Player 2 tied with {} points each!   |".format(player2score))
        print("\---------------------------------------------------/")
        # print("Player 1 and Player 2 tied with {} points each!".format(player1score))

    gamesPlayed += 1

    if gamesPlayed > 1:
        print("You have played {} games \n\tPlayer 1 has won {} games \n\tPlayer 2 has won {} games".format(gamesPlayed, player1GamesWon, player2GamesWon))
        if gamesPlayed > (player1GamesWon + player2GamesWon):
            # print(gamesPlayed)
            # print(player1GamesWon)
            # print(player2GamesWon)
            # print((gamesPlayed - (player1GamesWon + player2GamesWon)))
            if (gamesPlayed - (player1GamesWon + player2GamesWon)) == 1:
                print("\tThere has been 1 tie game")
            else:
                print("\tThere have been {} tie games".format(gamesPlayed - (player1GamesWon + player2GamesWon)))
    playAgain = input("Play again? (y/n) ")

