# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Andrew Lee
#               Johnson Pham
# Section:      engr-102-432
# Assignment:   Lab7a_Act3
# Date:         8 October 2020
# Topic:        Basic Chess simulator w/ nested lists

# INTRO
print("----WELCOME TO THE GAME OF FFA CHESS. YOU CONTROL EVERYTHING AND PIECES CAN MOVE WHEREVER AND HOWEVER YOU WANT!"
      "----\n---------- ENJOY!! ---------- \n")
# SIMULATION INSTRUCTIONS
print(" Valid coordinate inputs range from 1-8 for each axis. \n The X-axis are the rows on the board, "
      "the Y-axis are the columns on the board. \n If you wish to stop the game, type 'STOP' all caps into either move "
      "input query.")

# The chess board in its starting state
# x-axis:      A         B            C          D          E          F          G          H ||  # y-axis
board = [[chr(9814), chr(9816), chr(9815), chr(9813), chr(9812), chr(9815), chr(9816), chr(9814)], # 1
         [chr(9817), chr(9817), chr(9817), chr(9817), chr(9817), chr(9817), chr(9817), chr(9817)], # 2
         [    ".",       ".",       ".",       ".",       ".",       ".",       ".",       "."],   # 3
         [    ".",       ".",       ".",       ".",       ".",       ".",       ".",       "."],   # 4
         [    ".",       ".",       ".",       ".",       ".",       ".",       ".",       "."],   # 5
         [    ".",       ".",       ".",       ".",       ".",       ".",       ".",       "."],   # 6
         [chr(9823), chr(9823), chr(9823), chr(9823), chr(9823), chr(9823), chr(9823), chr(9823)], # 7
         [chr(9820), chr(9822), chr(9821), chr(9819), chr(9818), chr(9821), chr(9822), chr(9820)]] # 8

gameStatus = "GO"  # A flag that indicates to the while loop whether or not to continue running the game
didIError = False

# Displays the current state of the chess board
def displayBoard(boardToDisplay):
    # Iterates through and prints the nested arrays to look like a chess board
    print("--------------------------------------------------")
    print(" Current Board State:")
    for q in range(0, 8):
        print(" ", *boardToDisplay[q], sep="  ")

def convertLetterToNum(letter):
    if letter.capitalize() == "A":
        return 1
    elif letter.capitalize() == "B":
        return 2
    elif letter.capitalize() == "C":
        return 3
    elif letter.capitalize() == "D":
        return 4
    elif letter.capitalize() == "E":
        return 5
    elif letter.capitalize() == "F":
        return 6
    elif letter.capitalize() == "G":
        return 7
    elif letter.capitalize() == "H":
        return 8
    else:
        return 0

def isClearDirect(startingPt, endingPt):
    isWayClear = False
    # Need to find axis of movement
    if(startingPt[0] == endingPt[0]):
        # no x change, piece is moving on y-axis
        xAxis = startingPt[0]
        if startingPt[1] < endingPt[1]:
            # piece is moving up
            for y in range(1, abs(startingPt[1]-endingPt[1])):
                if board[xAxis][startingPt[1]+y] != ".":
                    print("the way is not clear")
                    isWayClear = False
        elif startingPt[1] > endingPt[1]:
            # piece is moving down
            for y in range(1, abs(startingPt[1]-endingPt[1])):
                if board[xAxis][startingPt[1]-y] != ".":
                    print("the way is not clear")
                    isWayClear = False
        else:
            print("the piece isn't moving, something's wrong [1]")
    elif(startingPt[1] == endingPt[1]):
        # no y change, piece is moving on x-axis
        yAxis = startingPt[1]
        if startingPt[0] < endingPt[0]:
            # piece is moving right
            for x in range(abs(startingPt[0]-endingPt[0])):
                if board[startingPt[0]+x][yAxis] != ".":
                    print("the way is not clear")
                    isWayClear = False
        elif startingPt[0] > endingPt[0]:
            # piece is moving left
            for x in range(abs(startingPt[0]-endingPt[0])):
                if board[startingPt[0]-x][yAxis] != ".":
                    print("the way is not clear")
                    isWayClear = False
        else:
            print("the piece isn't moving, something's wrong [2]")
    else:
        print("no x or y change found, something is wrong [3]")

    return isWayClear

def isMoveValid(startingPt, endingPt):
    moveValid = False
    # Identify piece type
    print("identify piece")
    if (ord(board[startingPt[1]][startingPt[0]]) == 9823) or (ord(board[startingPt[1]][startingPt[0]]) == 9817):
        # It's a pawn
        print("its a pawn")
        if board[endingPt[1]][endingPt[0]] == "." and startingPt[0] == endingPt[0] and (startingPt[1] == 1 or startingPt[1] == 6) and abs(endingPt[1]-startingPt[1]) <= 2:
            # legal straight ahead move (double move is an option)
            if abs(endingPt[1]-startingPt[1]) == 2:
                print("double move")
                # It is a double move
                if isClearDirect(startingPt, endingPt):
                    # The way is clear
                    print("the way is clear")
                    moveValid = True
                else:
                    print("not clear, cant double move")
                    moveValid = False
            else:
                print("legal straight ahead move of length {}".format(abs(endingPt[1]-startingPt[1])))
                moveValid = True
        elif board[endingPt[1]][endingPt[0]] == "." and startingPt[0] == endingPt[0] and abs(endingPt[1]-startingPt[1]) <= 1:
            # legal straight ahead move
            print("legal straight ahead move")
            moveValid = True
        elif (startingPt[0] != endingPt[0]) and (board[endingPt[1]][endingPt[0]] != "."):
            print("diagonal take")
            # diagonal take
            # determine piece color
            if (9818 <= ord(board[startingPt[1]][startingPt[0]]) <= 9823):
                # white piece
                if (9812 <= ord(board[endingPt[1]][endingPt[0]]) <= 9817):
                    # taking a black piece
                    print("diagonal take")
                    print("white piece taking a black piece")
                    moveValid = True
                else:
                    print("bruh, you can't take your own piece")
                    moveValid = False
            elif (9812 <= ord(board[startingPt[1]][startingPt[0]]) <= 9817):
                # black piece
                if (9818 <= ord(board[endingPt[1]][endingPt[0]]) <= 9823):
                    # taking a white piece
                    print("diagonal take")
                    print("black piece taking a white piece")
                    moveValid = True
                else:
                    print("bruh, you can't take your own piece")
                    moveValid = False
        else:
            print("illegal pawn move!")
            moveValid = False
        return moveValid
    elif (ord(board[startingPt[1]][startingPt[0]]) == 9820) or (ord(board[startingPt[1]][startingPt[0]]) == 9814):
        print("its a rook")
        # It's a rook
        if startingPt[0] == endingPt[0] and startingPt[1] != endingPt[1]:
            # straight ahead y move
            if abs(startingPt[1]-endingPt[1]) > 1:
                # The move is more than 1 square
                if isClearDirect(startingPt, endingPt):
                    moveValid = True
                else:
                    moveValid = False
            else:
                moveValid = True
        elif startingPt[1] == endingPt[1] and startingPt[0] != endingPt[0]:
            # straight ahead x move
            if abs(startingPt[0] - endingPt[0]) > 1:
                # The move is more than 1 square
                if isClearDirect(startingPt, endingPt):
                    moveValid = True
                else:
                    moveValid = False
            else:
                moveValid = True
        else:
            moveValid = False

        return moveValid
    # need to check for bishop
        # need to have bishop move check (can modify isClearDirect() for that)
    # need to check for knight
        # need to have knight move check (new method)
    # need to check for queen
        # need to have queen move check (the bishop modification should handle this)
    # need to check for king
        # need to have king move check (can do within isMoveValid())
    else:
        didIError = True
        return False

# The loop inside which the game runs -- runs the loop until the gameStatus is changed from "GO" to "STOP"
while gameStatus != "STOP":
    # Display the current state of the board
    displayBoard(board)

    # Ask the user for board coordinates of the desired piece's current location and desired end location
    startMove = input(" Enter the coordinates of the piece you want to move (row column):")
    if startMove.upper() == "STOP":
        # If the user did stop the game, tell the while loop to stop and tell the user the game has stopped
        gameStatus = "STOP"
        print("You have stopped the game")
        break
    endMove = input(" Enter the coordinates of where you want to move the piece (row column):")
    if endMove.upper() == "STOP":
        # If the user did stop the game, tell the while loop to stop and tell the user the game has stopped
        gameStatus = "STOP"
        print("You have stopped the game")
        break

    # Check to make sure the user didn't end the game
    if startMove.capitalize() == "STOP" or endMove.capitalize() == "STOP":
        # If the user did stop the game, tell the while loop to stop and tell the user the game has stopped
        gameStatus = "STOP"
        print("You have stopped the game")
        break
    # -- THE MAIN BODY OF THE CODE THAT RUNS OVER AND OVER --
    else:
        # Turn the user-inputted strings into arrays (start and end)
        inputPtStart = startMove.split(" ")
        inputPtEnd = endMove.split(" ")

        startPt = []
        endPt = []

        # Convert user-inputted chess positions to numerical positions
        startPt.append(convertLetterToNum(inputPtStart[0]))
        startPt.append(int(inputPtStart[1]))
        endPt.append(convertLetterToNum(inputPtEnd[0]))
        endPt.append(int(inputPtEnd[1]))

        # # Convert the elements in the start point array from strings to ints
        # for i in inputPtStart:
        #     startPt.append(int(i))
        # Convert the elements in the end point array from strings to ints
        # for p in inputPtEnd:
        #     endPt.append(int(p))

        pt1Valid = True
        pt2Valid = True
        # Checking to make sure the start point is within the accepted bounds
        if min(startPt) < 1 or max(startPt) > 8:
            print("\n Sorry! You inputted an invalid first point!\n Remember, 1-8 are the accepted values.")
            pt1Valid = False
        # Checking to make sure the end point is within the accepted bounds
        if min(endPt) < 1 or max(endPt) > 8:
            print("\n Sorry! You inputted an invalid second point!\n Remember, 1-8 are the accepted values.")
            pt2Valid = False

        # Continue if both points are valid
        if pt1Valid and pt2Valid:
            # Adjusting the value of the inputs from the 8-1 range of the chess board to the 0-7 range of the arrays
            # print(startPt)
            # print(endPt)
            startPt[0] = startPt[0] - 1
            startPt[1] = abs(startPt[1] - 8)
            endPt[0] = endPt[0] - 1
            endPt[1] = abs(endPt[1] - 8)
            # print(startPt)
            # print(ord(board[startPt[0]][startPt[0]]))
            # print(endPt)

            # This part actually "moves" the piece to the desired position
            # Assign the end point value on the board with the starting point value of the board
            #   (the piece moves to the end point)
            if(isMoveValid(startPt, endPt)):
                board[endPt[1]][endPt[0]] = board[startPt[1]][startPt[0]]
            # Overwrite the starting point value of the board with a dot
            #   (signifies that the starting point is now empty)
                board[startPt[1]][startPt[-0]] = "."
                print("Did I Error? ", didIError)
            else:
                print("Invalid Move! Learn the rules dude..")



