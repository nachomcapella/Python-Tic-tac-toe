#This code was made during the course Python Bootcamp 2020 Build 15 working Applications and Games.
#Please, check the course at https://www.udemy.com/course/python-complete-bootcamp-2019-learn-by-applying-knowledge/
#for the original version of the code.

#First, we define the board as a list of 9 empty spaces. The player and the computer will fill the board positions them with their values.
board = [' ' for x in range(10)]

#This function prints the actual state of the board.
def printBoard(board):
    print(" ")
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3])
    print("---|---|---|")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6])
    print("---|---|---|")
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9])
    print(" ")

#When the user or the computer chooses a position in the board, we change the value of that position to the code of the actual player. 
def choosePosition(userCode,position):
    board[position] = userCode

#Of course, only empty positions should be available for the players, so we need a function to check this.
def isPositionFree(position):
    if board[position] == ' ':
        return True
    else:
        return False

#The game can end when the user or the computer connects three positions in a row or when there are no positions left. This function checks this last scenario by counting the empty positions.
def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

#This function checks if there is any of the possible combinations of three positions in a row with the same user code. If there is, then that user wins.
def isWinner(board,userCode):
    if((board[1]==userCode and board[2]==userCode and board[3]==userCode)
      or (board[4]==userCode and board[5]==userCode and board[6]==userCode)
      or (board[7]==userCode and board[8]==userCode and board[9]==userCode)
      or (board[1]==userCode and board[4]==userCode and board[7]==userCode)
      or (board[2]==userCode and board[5]==userCode and board[8]==userCode)
      or (board[3]==userCode and board[6]==userCode and board[9]==userCode)
      or (board[1]==userCode and board[5]==userCode and board[9]==userCode)
      or (board[3]==userCode and board[5]==userCode and board[7]==userCode)):
        return True
    else:
        return False

 #This code is used to select the user position.
def playerPosition():
    run = True
    while(run):
        position = input("Please, select a position (1-9): ")
        try:
            position = int(position) #Check that the user wrote an integer value.
            if(position > 0 and position < 10): #Check that the integer is between 1 and 9 (only 9 positions in the board).
                if(isPositionFree(position)): #Check that the computer has not chosen that position already.
                    choosePosition('X',position)
                    run = False;
                else:
                    print("Sorry, this space is occupied.")
            else:
                print("Please, enter a valid position (1-9)")
        except:
            print("Please, type a number!")

#And now, the computer's turn.            
def computerPosition():
    possiblePositions = [x for x, code in enumerate(board) if code == ' ' and x!=0] #Get the empty positions.
    position = 0 #Choose one by default (note that 0 is not between 1 and 9 so it is not a valid option).

    #For every code value, we check every available position to see if choosing it would mean that the computer wins.
    for code in ['O','X']:
        for i in possiblePositions:
            board_copy = board[:] #Get a copy of the board.
            board_copy[i] = code #Select the available position.
            if (isWinner(board_copy,code)): #If it is a winner position, we choose it.
                position = i
                return position

    #Next, if the previous attempt did not work, we check if there is any free position in the corners of the board.
    freeCorners = []
    for i in possiblePositions: #Using the available positions, we keep only those corresponding to the corners.
        if i in [1,3,7,9]
            freeCorners.append(i)
        if len(freeCorners) > 0: #If there is any available, we choose our position randomly.
            position = selectRandomPosition(freeCorners)
            return position

    #If there was no free corner left, we choose the central position of the board.
    if 5 in possiblePositions:
        position = 5
        return position

    #If the centre was also taken, we select among the remaining positions, the centres of the edges.
    freeEdges = []
    for i in possiblePositions:
        if i in [2,4,6,8]:
            freeEdges.append(i)
        if len(freeEdges) > 0:
            position = selectRandomPosition(freeEdges)
            return position

    #If no position has been selected until now, we return the impossible value 0, selected at the beginning of the function.
    return position

#This function just selects a random position from a given list.
def selectRandomPosition(positions):
    import random
    ln = len(positions)
    r = random.randrange(0,ln)
    return positions[r]

#The main function of the game.
def tictactoe():
    #First, the title.
    print("---------------------------------------")
    print("| * WELCOME TO THE TIC-TAC-TOE GAME * |")
    print("---------------------------------------")
    printBoard(board) #Let's print the empty board.
    while(not(isBoardFull(board))): #We will play until the board is full (or a player wins).
          if(not(isWinner(board,'O'))): #We start by checking if the computer has won. If not, the user must choose a position.
              playerPosition()
              printBoard(board) #After each turn, we print the state of the board.
          else:
              print("The computer won :(") #Sorry, man.
              break

          if(not(isWinner(board,'X'))): #We repeat the process for the computer, by checking if the user has won.
              position = computerPosition()
              if position == 0: #If the computer chooses the position 0 (not valid), that means there are no positions left. So we have a tie game.
                  print("Tie game!")
                  break
              else:
                  choosePosition('O',position)
                  print("The computer chose position ",position,": ")
                  printBoard(board)
          else:
              print("You won :)")
              break

#This remaining lines of code start the game, asking the user if he wants to play and resetting the board.
while(True):
    play = input("Do you want to start a new game? (y/n): ")
    if play == 'y':
        board = [' ' for x in range(10)]
        print(' ')
        tictactoe()
    else:
        print("Goodbye!")
        break
