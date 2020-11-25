board = [' ' for x in range(10)]

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

def choosePosition(userCode,position):
    board[position] = userCode

def isPositionFree(position):
    if board[position] == ' ':
        return True
    else:
        return False

def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

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

def playerPosition():
    run = True
    while(run):
        position = input("Please, select a position (1-9): ")
        try:
            position = int(position)
            if(position > 0 and position < 10):
                if(isPositionFree(position)):
                    choosePosition('X',position)
                    run = False;
                else:
                    print("Sorry, this space is occupied.")
            else:
                print("Please, enter a valid position (1-9)")
        except:
            print("Please, type a number!")

def computerPosition():
    possiblePositions = [x for x, code in enumerate(board) if code == ' ' and x!=0]
    position = 0

    for code in ['O','X']:
        for i in possiblePositions:
            board_copy = board[:]
            board_copy[i] = code
            if (isWinner(board_copy,code)):
                position = i
                return position

    freeCorners = []
    for i in possiblePositions:
        if i in [1,3,7,9]:
            freeCorners.append(i)
        if len(freeCorners) > 0:
            position = selectRandomPosition(freeCorners)
            return position

    if 5 in possiblePositions:
        position = 5
        return position

    freeEdges = []
    for i in possiblePositions:
        if i in [2,4,6,8]:
            freeEdges.append(i)
        if len(freeEdges) > 0:
            position = selectRandomPosition(freeEdges)
            return position

    return position

def selectRandomPosition(positions):
    import random
    ln = len(positions)
    r = random.randrange(0,ln)
    return positions[r]

def tictactoe():
    print("---------------------------------------")
    print("| * WELCOME TO THE TIC-TAC-TOE GAME * |")
    print("---------------------------------------")
    printBoard(board)
    while(not(isBoardFull(board))):
          if(not(isWinner(board,'O'))):
              playerPosition()
              printBoard(board)
          else:
              print("The computer won :(")
              break

          if(not(isWinner(board,'X'))):
              position = computerPosition()
              if position == 0:
                  print("Tie game!")
                  break
              else:
                  choosePosition('O',position)
                  print("The computer chose position ",position,": ")
                  printBoard(board)
          else:
              print("You won :)")
              break
        
while(True):
    play = input("Do you want to start a new game? (y/n): ")
    if play == 'y':
        board = [' ' for x in range(10)]
        print(' ')
        tictactoe()
    else:
        print("Goodbye!")
        break
    #board = [' ' for x in range(10)]
    #tictactoe()
