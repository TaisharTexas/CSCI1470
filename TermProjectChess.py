# INTRO
print("----WELCOME TO THE GAME OF FFA CHESS. YOU CONTROL EVERYTHING AND PIECES CAN MOVE WHEREVER AND HOWEVER YOU WANT!"
      "----\n---------- ENJOY!! ---------- \n")
# SIMULATION INSTRUCTIONS
print(" Valid coordinate inputs range from 1-8 for each axis. \n The X-axis are the rows on the board, "
      "the Y-axis are the columns on the board. \n If you wish to stop the game, type 'STOP' into either move input "
      "query.")

# The chess board in its starting state
# x-axis: A(1 -> 0)  B(2 -> 1)  C(3 -> 2)  D(4 -> 3)  E(5 -> 4)  F(6 -> 5)  G(7 -> 6)  H(8 -> 7) ||# y-axis
board = [[chr(9814), chr(9816), chr(9815), chr(9813), chr(9812), chr(9815), chr(9816), chr(9814)], # 1 -> 0
         [chr(9817), chr(9817), chr(9817), chr(9817), chr(9817), chr(9817), chr(9817), chr(9817)], # 2 -> 1
         [    ".",       ".",       ".",       ".",       ".",       ".",       ".",       "."],   # 3 -> 2
         [    ".",       ".",       ".",       ".",       ".",       ".",       ".",       "."],   # 4 -> 3
         [    ".",       ".",       ".",       ".",       ".",       ".",       ".",       "."],   # 5 -> 4
         [    ".",       ".",       ".",       ".",       ".",       ".",       ".",       "."],   # 6 -> 5
         [chr(9823), chr(9823), chr(9823), chr(9823), chr(9823), chr(9823), chr(9823), chr(9823)], # 7 -> 6
         [chr(9820), chr(9822), chr(9821), chr(9819), chr(9818), chr(9821), chr(9822), chr(9820)]] # 8 -> 7

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


def isWhite(startingPt):
    if (9818 <= ord(board[startingPt[1]][startingPt[0]]) <= 9823):
        print("white piece")
        return True
    else:
        print("black piece")
        return False


def legalTake(startingPt, endingPt):
    if (9818 <= ord(board[startingPt[1]][startingPt[0]]) <= 9823) and not (9818 <= ord(board[endingPt[1]][endingPt[0]]) <= 9823):
        print("its a white piece")
        moveValid = True
    elif (9812 <= ord(board[startingPt[1]][startingPt[0]]) <= 9817) and not (9812 <= ord(board[endingPt[1]][endingPt[0]]) <= 9817):
        print("its a black piece")
        moveValid = True
    else:
        print("you cant take your own piece")
        moveValid = False

    return moveValid


def isClearDirect(startingPt, endingPt):
    isWayClear = True
    # Need to find axis of movement
    if(startingPt[0] == endingPt[0]):
        # no x change, piece is moving on y-axis
        print("no x change, y axis movement")
        xAxis = startingPt[0]
        print("startingPt (x,y): ({},{})".format(startingPt[0], startingPt[1]))
        print("endingPt (x,y): ({},{})".format(endingPt[0], endingPt[1]))
        if startingPt[1] > endingPt[1]:
            # piece is moving up
            print("moving up")
            for y in range(1, abs(startingPt[1]-endingPt[1])):
                print("entered for loop")
                print(abs(startingPt[1]-endingPt[1]))
                print(y)
                print("board at startingPt: {}".format(board[startingPt[1]][xAxis]))
                print("board at startingPt+y: {}".format(board[startingPt[1]-y][xAxis]))
                if board[startingPt[1]-y][xAxis] != ".":
                    print("the way is not clear")
                    isWayClear = False
                else:
                    print("nothing flagged, way is clear")
        elif startingPt[1] < endingPt[1]:
            # piece is moving down
            print("moving down")
            for y in range(1, abs(startingPt[1]-endingPt[1])):
                print("entered for loop")
                print(abs(startingPt[1]-endingPt[1]))
                print(y)
                print("board at startingPt: {}".format(board[startingPt[1]][xAxis]))
                print("board at startingPt-y: {}".format(board[startingPt[1]+y][xAxis]))
                if board[startingPt[1]+y][xAxis] != ".":
                    print("the way is not clear")
                    isWayClear = False
                else:
                    print("nothing flagged, way is clear")
        else:
            print("the piece isn't moving, something's wrong [1]")
    elif(startingPt[1] == endingPt[1]):
        # no y change, piece is moving on x-axis
        print("no y change, x axis movement")
        yAxis = startingPt[1]
        if startingPt[0] < endingPt[0]:
            # piece is moving right
            print("moving right")
            for x in range(1, abs(startingPt[0]-endingPt[0])):
                print("entered for loop")
                print(abs(startingPt[0]-endingPt[0]))
                print(x)
                print("board at startingPt: {}".format(board[yAxis][startingPt[0]]))
                print("board at startingPt+x: {}".format(board[yAxis][startingPt[0]+x]))
                if board[yAxis][startingPt[0]+x] != ".":
                    print("the way is not clear")
                    isWayClear = False
        elif startingPt[0] > endingPt[0]:
            # piece is moving left
            print("moving left")
            for x in range(1, abs(startingPt[0]-endingPt[0])):
                print("entered for loop")
                print(abs(startingPt[0]-endingPt[0]))
                print(x)
                print("board at startingPt: {}".format(board[yAxis][startingPt[0]]))
                print("board at startingPt-x: {}".format(board[yAxis][startingPt[0]-x]))
                if board[yAxis][startingPt[0]-x] != ".":
                    print("the way is not clear")
                    isWayClear = False
        else:
            print("the piece isn't moving, something's wrong [2]")
    elif (startingPt[0] != endingPt[0]) and (startingPt[1] != endingPt[1]):
        # changes in both axis, diagonal movement
        print("diagonal move")
        if startingPt[1] > endingPt[1]:
            # moving up
            print("up and to the", end=" ")
            if startingPt[0] > endingPt[0]:
                # moving left
                print("left")
                for m in range(1, abs(startingPt[0] - endingPt[0])):
                    if board[startingPt[1]-m][startingPt[0]+m] != ".":
                        print("the way is not clear")
                        isWayClear = False
            else:
                # moving right
                print("right")
                for m in range(1, abs(startingPt[0] - endingPt[0])):
                    if board[startingPt[1]-m][startingPt[0]+m] != ".":
                        print("the way is not clear")
                        isWayClear = False
        else:
            # moving down
            print("down and to the", end=" ")
            if startingPt[0] < endingPt[0]:
                # moving left
                print("left")
                for m in range(1, abs(startingPt[0] - endingPt[0])):
                    if board[startingPt[1]+m][startingPt[0]-m] != ".":
                        print("the way is not clear")
                        isWayClear = False
            else:
                # moving right
                print("right")
                for m in range(1, abs(startingPt[0] - endingPt[0])):
                    if board[startingPt[1]+m][startingPt[0]+m] != ".":
                        print("the way is not clear")
                        isWayClear = False
    else:
        print("no x or y change found, something is wrong [3]")

    return isWayClear


def isMoveValid(startingPt, endingPt):
    moveValid = False
    # Identify piece type
    print("identify piece")

    # BOARD[y][x]
    if (ord(board[startingPt[1]][startingPt[0]]) == 9823) or (ord(board[startingPt[1]][startingPt[0]]) == 9817):
        # It's a pawn
        print("its a pawn")
        if board[endingPt[1]][endingPt[0]] == "." and startingPt[0] == endingPt[0] and (startingPt[1] == 1 or startingPt[1] == 6) and abs(endingPt[1]-startingPt[1]) <= 2:
            # legal straight ahead move (double move is an option)
            print(endingPt[1]-startingPt[1])
            if (isWhite(startingPt) and (endingPt[1]-startingPt[1] < 0)) or (not(isWhite(startingPt)) and (endingPt[1]-startingPt[1]) > 0):
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
            else:
                moveValid = False
                print("Pawns don't move backwards genius")
        elif board[endingPt[1]][endingPt[0]] == "." and startingPt[0] == endingPt[0] and abs(endingPt[1]-startingPt[1]) <= 1:
            if (isWhite(startingPt) and (endingPt[1] - startingPt[1] < 0)) or (not (isWhite(startingPt)) and (endingPt[1] - startingPt[1]) > 0):
                # legal straight ahead move
                print("legal straight ahead move")
                moveValid = True
            else:
                moveValid = False
                print("pawns don't move backwards genius")
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
                if isClearDirect(startingPt, endingPt) and legalTake(startingPt, endingPt):
                    moveValid = True
                else:
                    moveValid = False
            else:
                moveValid = True
        elif startingPt[1] == endingPt[1] and startingPt[0] != endingPt[0]:
            # straight ahead x move
            if abs(startingPt[0] - endingPt[0]) > 1:
                # The move is more than 1 square
                if isClearDirect(startingPt, endingPt) and legalTake(startingPt, endingPt):
                    moveValid = True
                else:
                    moveValid = False
            else:
                moveValid = True
        else:
            moveValid = False

        return moveValid
    elif (ord(board[startingPt[1]][startingPt[0]]) == 9821) or (ord(board[startingPt[1]][startingPt[0]]) == 9815):
        print("its a bishop")
        return isClearDirect(startingPt, endingPt) and legalTake(startingPt, endingPt)
    elif (ord(board[startingPt[1]][startingPt[0]]) == 9816) or (ord(board[startingPt[1]][startingPt[0]]) == 9822):
        print("its a knight")
        if ((abs(startingPt[1]-endingPt[1]) == 2) and (abs(startingPt[0]-endingPt[0]) == 1)) or ((abs(startingPt[1]-endingPt[1]) == 1) and (abs(startingPt[0]-endingPt[0]) == 2)):
            return legalTake(startingPt, endingPt)
        else:
            print("illegal knight move")
            return False
    # need to check for queen
    elif (ord(board[startingPt[1]][startingPt[0]]) == 9819) or (ord(board[startingPt[1]][startingPt[0]]) == 9813):
        print("its a queen")
        return isClearDirect(startingPt, endingPt) and legalTake(startingPt, endingPt)
    elif (ord(board[startingPt[1]][startingPt[0]]) == 9818) or (ord(board[startingPt[1]][startingPt[0]]) == 9812):
        print("its a king")
        return legalTake(startingPt, endingPt)
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
        if endMove.upper() == "DELETE":
            inputPtStart = startMove.split(" ")
            startPt = []
            startPt.append(convertLetterToNum(inputPtStart[0]))
            startPt.append(int(inputPtStart[1]))
            if min(startPt) < 1 or max(startPt) > 8:
                print("\n Sorry! You inputted an invalid first point!\n Remember, 1-8 are the accepted values.")
            else:
                startPt[0] = startPt[0] - 1  # x-axis
                startPt[1] = abs(startPt[1] - 8)  # y-axis

                board[startPt[1]][startPt[-0]] = "."
        else:
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
                print(startPt)
                print(endPt)
                startPt[0] = startPt[0] - 1 # x-axis
                startPt[1] = abs(startPt[1] - 8) # y-axis
                endPt[0] = endPt[0] - 1 # x-axis
                endPt[1] = abs(endPt[1] - 8) #y-axis
                print("final start pt: {}".format(startPt))
                # print(ord(board[startPt[0]][startPt[0]]))
                print("final end pt: {}".format(endPt))

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



