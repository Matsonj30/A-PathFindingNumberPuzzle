import copy
from typing import Match
def initializeBoard():
   board = []
   row = []
   goalState = [[0,1,2],[3,4,5],[6,7,8]]
   boardInput =  input("Enter nine numbers")
   for number in range(18):
        if number % 2 == 0:
            row.append(int(boardInput[number]))       
        if len(row) == 3:
            board.append(row)
            row = []
   print("(Initial)")
   solvePuzzle(board, goalState)


def printboard(board):
    for row in board:
        for value in row:
            if value == 0:
                print("  ", end='')
            else:
                print(str(value) + " ", end='')
        print("")


def solvePuzzle(boardState, goalState):
    test = 10 #########################################
    alreadyTraveledStates = []
    GValue = 0
    AStarQueue = [boardState, GValue]
    goalFound = False
    #while(len(AStarQueue) != 0):
    while(test > 1):
        test -= 1 
        GValue += 1
        nextAction = AStarQueue.pop(0)
        AStarQueue.pop(0)
        AStarQueue = []
        alreadyTraveledStates.append(nextAction)
        #print(alreadyTraveledStates)
        if(nextAction == goalState):
            print("DONE")
            printboard(nextAction)
            goalFound = True
            break
        else:
            printboard(nextAction)
            print(" ")
            for action in possibleActions(nextAction, GValue , alreadyTraveledStates):
                    AStarQueue.append(action)
            AStarQueue = sortQueueUsingManhattan(AStarQueue, GValue)
    if(goalFound == False):
        print("No solution")
def sortQueueUsingManhattan(queue, Gvalue):
    #f(n) = g(n) + h(n)
    HValue = 0
    FValue = 0
    sortedQueue = []
    oneGoal = (0,1)
    twoGoal = (0,2)
    threeGoal = (1,0)
    fourGoal = (1,1)
    fiveGoal = (1,2)
    sixGoal = (2,0)
    sevenGoal = (2,1)
    eightGoal = (2,2)
    print(queue)
    print("^^^^ START")

    for state in queue:
        HValue = 0
        FValue = 0
        if(type(state) == list):
            print(state)
            for row in range(3):
               for col in range(3):
                   if state[row][col] == 1:
                       HValue += abs(oneGoal[0] - row)
                       HValue += abs(oneGoal[1] - col)
                   elif state[row][col] == 2:
                       HValue += abs(twoGoal[0] - row)
                       HValue += abs(twoGoal[1] - col)
                   elif state[row][col] == 3:
                       HValue += abs(threeGoal[0] - row)
                       HValue += abs(threeGoal[1] - col)
                   elif state[row][col] == 4:
                       HValue += abs(fourGoal[0] - row)
                       HValue += abs(fourGoal[1] - col)
                   elif state[row][col] == 5:
                       HValue += abs(fiveGoal[0] - row)
                       HValue += abs(fiveGoal[1] - col)
                   elif state[row][col] == 6:
                       HValue += abs(sixGoal[0] - row)
                       HValue += abs(sixGoal[1] - col)
                   elif state[row][col] == 7:
                       HValue += abs(sevenGoal[0] - row)
                       HValue += abs(sevenGoal[1] - col)
                   elif state[row][col] == 8:
                       HValue += abs(eightGoal[0] - row)
                       HValue += abs(eightGoal[1] - col)

            FValue = Gvalue + HValue
            print(FValue)
            if(len(sortedQueue)) == 0: #if the sortedQueue is empty, jsut insert it
                sortedQueue.append(state) 
                sortedQueue.append(FValue)
            else:
                valueInserted = False
                for i in range(len(sortedQueue)): #iterate through sortedqueue
                    if(type(sortedQueue[i]) == int): #if we find previous HValue
                        if(sortedQueue[i] >= FValue): #if sortedQueue F value is greater than our current vlaue
                           # print(HValue)
                            sortedQueue.insert((i - 1), FValue) #insert current value in front of that value
                            sortedQueue.insert((i- 1), state)
                            valueInserted = True
                if(valueInserted == False):
                    sortedQueue.append(state)
                    sortedQueue.append(FValue)
                    print("APPENDED END")
    print(sortedQueue)
    return(sortedQueue)


def possibleActions(currentState, Gvalue, alreadyTraveledStates):
    possibleActionsList = []
    NewZeroLocations = []
    ZeroRow = -1 
    ZeroCol = -1
    for row in range(3):  #find where the empty spot is
        for col in range(3):
            if currentState[row][col] == 0:
                ZeroRow = row
                ZeroCol = col

    
    moveZeroUp = [ZeroRow -1, ZeroCol] #get the coords for where the 0 could possibly be
    moveZeroDown = [ZeroRow + 1, ZeroCol]
    moveZeroRight = [ZeroRow, ZeroCol + 1]
    moveZeroLeft = [ZeroRow, ZeroCol - 1]
    #boundary check
    if(moveZeroUp[0] > -1):
        NewZeroLocations.append(moveZeroUp)
    if(moveZeroDown[0] < 3):
        NewZeroLocations.append(moveZeroDown)
    if(moveZeroRight[1] < 3):
        NewZeroLocations.append(moveZeroRight)
    if(moveZeroLeft[1] > -1):
        NewZeroLocations.append(moveZeroLeft)
    #these are the places the empty stone can move
    #take the input list, "alter" it, put in new list
    for option in NewZeroLocations:
        possibleActionTemp = copy.deepcopy(currentState)  #giving same address 
        temp = currentState[option[0]][option[1]] #get value that is to be swapped with 0
        possibleActionTemp[option[0]][option[1]] = 0 #put zero into that spot
        possibleActionTemp[ZeroRow][ZeroCol] = temp #put the temporary value into the zero position
        if(possibleActionTemp not in alreadyTraveledStates):
                #print(possibleActionTemp)
                #print(alreadyTraveledStates)
                possibleActionsList.append(possibleActionTemp)
                possibleActionsList.append(Gvalue)
    #print(possibleActionsList)
    return(possibleActionsList)

print(sortQueueUsingManhattan([[[3, 1, 2], [6, 0, 5], [7, 4, 8]], 1, [[3, 1, 2], [6, 4, 5], [7, 8, 0]], 1, [[3, 1, 2], [6, 4, 5], [0, 7, 8]], 1], 1))
#print(possibleActions([[3,1,2],[0,4,5],[6,7,8]], 1, [[[3,1,2],[6,4,5],[0,7,8]]]))
#initializeBoard()

#[[[3, 1, 2], [4, 0, 5], [6, 7, 8]], 2, [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 3] is output in algo