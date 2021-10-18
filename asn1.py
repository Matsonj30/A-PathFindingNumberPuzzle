def initializeBoard():
   board = []
   row = []
   boardInput =  input("Enter nine numbers")
   for number in range(18):
        if number % 2 == 0:
            row.append(int(boardInput[number]))       
        if len(row) == 3:
            board.append(row)
            row = []
   print("(Initial)")
   solvePuzzle(board)


def printboard(board):
    for row in board:
        for value in row:
            if value == 0:
                print("  ", end='')
            else:
                print(str(value) + " ", end='')
        print("")


def solvePuzzle(boardState):
    printboard(boardState) 
    alreadyTraveledStates = [boardState]
    AStarQueue = [boardState]
    while(len(AStarQueue) != 0):
        for action in possibleActions(AStarQueue.pop(0)):
            AStarQueue.append(action)

    
## Given a state, will print all possible actions
def possibleActions(currentState):
    possibleActionsList = []
    NewZeroLocations = []
    ZeroRow = -1 
    ZeroCol = -1
    for row in range(3):
        for col in range(3):
            if currentState[row][col] == 0:
                ZeroRow = row
                ZeroCol = col

    
    moveZeroUp = [ZeroRow -1, ZeroCol]
    moveZeroDown = [ZeroRow + 1, ZeroCol]
    moveZeroRight = [ZeroRow, ZeroCol + 1]
    moveZeroLeft = [ZeroRow, ZeroCol - 1]
    
    

    if(moveZeroUp[0] > -1):
        NewZeroLocations.append(moveZeroUp)
    if(moveZeroDown[0] < 3):
        NewZeroLocations.append(moveZeroDown)
    if(moveZeroRight[1] < 3):
        NewZeroLocations.append(moveZeroRight)
    if(moveZeroLeft[1] > -1):
        NewZeroLocations.append(moveZeroLeft)
    #these are the places the empty stone can move
    #take the input list, "alter" it, put in new list, keep temp somehow?
    for option in NewZeroLocations:
        possibleActionTemp = currentState  #giving same address 
        print(hex(id(possibleActionTemp)))
        print(hex(id(currentState)))
        temp = currentState[option[0]][option[1]] #get value that is to be swapped with 0
        possibleActionTemp[option[0]][option[1]] = 0 #put zero into that spot
        possibleActionTemp[ZeroRow][ZeroCol] = temp #put the temporary value into the zero position
        possibleActionsList.append(possibleActionTemp)
        
        possibleActionTemp[ZeroRow][ZeroCol] = 0 #go backwards to fix address issue
        possibleActionTemp[option[0]][option[1]] = temp

    print(possibleActionsList)
possibleActions([[9,2,3], [8,0,5],[7,1,6]])

#initializeBoard()

