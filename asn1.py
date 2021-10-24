import copy
from os import path, stat
from typing import Match
# Jared Matson
# #1570490
# Asn1.py
# ***CURRENTLY RUNS infinitely, instruction on Eclass makes it look like the program will constantly ask for states to solve***

# Given 9 numbers from 0-8 (e.g 1 8 2 0 4 3 7 6 5) will return said numbers as an initial state
#[1 8 2]
#[2   4]
#[7 6 5]
#for the 1-8 puzzle game. The program will then use A* pathfinding to find the least amount of steps to reach
#the goal state by sliding the blocks up/down/left/right
#[0 1 2]
#[3 4 5]
#[6 7 8]

#class Node
#This class represents a possible state in the puzzle
# value = the value of the Node e.g
#[1 8 2]
#[2   4]
#[7 6 5]
#gvalue = the gValue of the Node, e.g the amount of moves it took to get to that state
#parent = the parent Node or previous state of the node
#direction = Direction the empty spot had to move to reach Node
class Node:
    def __init__(self, value, gvalue, parent, direction) -> None:
        self.value = value
        self.parent = parent
        self.h = 0
        self.f = 0
        self.g = gvalue
        self.direction = direction

# def InitializeBoard()
# Takes an input from the user e.g (e.g 1 8 2 0 4 3 7 6 5) and will create a 2d
# array with the values to represent the puzzle
def initializeBoard():
   board = []
   row = []
   goalState = [[0,1,2],[3,4,5],[6,7,8]]
   boardInput =  input("Enter nine numbers")
   for number in range(18): #going around spaces
        if number % 2 == 0:
            row.append(int(boardInput[number]))       
        if len(row) == 3: #create new row if 3 numbers already in the current row
            board.append(row)
            row = []
   start = Node(board,0,None, "N/A") #initialize root of tree
   solvePuzzle(start, goalState)

# def printBoard(board)
# Will iterate through the puzzle (2d array) and will print the 
# values to better represent what the 8 number puzzle actually looks like

# Parameters:
# board - the board being printed

# Returns:
# N/A
def printboard(board):
    for row in board:
        for value in row:
            if value == 0:
                print("  ", end='')
            else:
                print(str(value) + " ", end='')
        print("")

# def solvePuzzle(boardState, goalState)
# Controls the flow of the program, will call upon multiple functions to find appropriate moves in the puzzle, as well
# as which one is most optimal using A*

# Parameters:
# boardState - the initial state wanting to be solved
# goalState - the goal state wanting to be reached

# Returns:
# N/A
def solvePuzzle(boardState, goalState):
    alreadyTraveledStates = [] #Previous states
    nextMoveList = [] #list of possible next moves in a given state
    GValue = 0
    AStarQueue = [boardState] 
    goalFound = False
    while(len(AStarQueue) != 0):
        nextAction = AStarQueue.pop(0)
        alreadyTraveledStates.append(nextAction) #if value is popped out of AStarQueue, we know it is now an already travelled state
        GValue = nextAction.g + 1
        if(nextAction.value == goalState):
            printGoalPath(nextAction) #print solution path
            goalFound = True
            break
        else:
            for action in possibleActions(nextAction, alreadyTraveledStates, GValue): #find the possible actions in the current state, not including previously traversed states
                    nextMoveList.append(action)
            AStarQueue = sortQueueUsingManhattan(AStarQueue, nextMoveList) #sort the newly found nodes into the AStarQueue 
            nextMoveList.clear()#newly found nodes have been appended, now we dont need them anymore
            
    if(goalFound == False):
        print("No solution")

# def printGoalPath(goalNode)
# Since the goalNode has been found, the path to get to this Node can easily be printed by printing each Nodes parent until we reach the root

# Parameters:
# goalNode - the goal Node that was found

# Returns:
# N/A
def printGoalPath(goalNode):
    pathList = []
    while(goalNode.parent != None):       #We are at the bottom of the tree, and we want to print from the top down, not the bottom up
        pathList.insert(0,goalNode) #We can easier print the states from the root to the goal node if we just add it to a list to flip the order
        goalNode = goalNode.parent
    pathList.insert(0,goalNode) #add root node
    print("(Initial)")
    for i in range(len(pathList)): #Print now in order list
        print("Move "+ str(i),end="")
        print(" (Move blank tile ",end="")
        print(pathList[i].direction,end="")
        print(")")
        printboard(pathList[i].value)
        print(" ")
    print("============================")
    print("Total number of moves: " + str(len(pathList) - 1))
    print("============================")
    
# def sortQueueUsingMangattan(queue, movesToSortIntoQueue)
# given the current AStarQueue and the potential states that can be taken,
# will use A* to move the potential states into the prexisting AStarQueue

# Parameters:
# queue - the curent A* queue
# movesToSortIntoQueue - potential states that can be taken from the current node

# Returns:
# updated A* queue 
def sortQueueUsingManhattan(queue, movesToSortIntoQueue):
    #f(n) = g(n) + h(n)
    HValue = 0
    FValue = 0
    #list of coordinates for each number in their goal state
    oneGoal = (0,1)
    twoGoal = (0,2)
    threeGoal = (1,0)
    fourGoal = (1,1)
    fiveGoal = (1,2)
    sixGoal = (2,0)
    sevenGoal = (2,1)
    eightGoal = (2,2)
    for state in movesToSortIntoQueue:#for each move that can be taken
        value = state.value #grab the 2d array value from the Node
        HValue = 0
        FValue = 0
        #iterate through the 2d array, when you find each number, calculate manhattan distance
        for row in range(3):
            for col in range(3):
                if value[row][col] == 1:
                    HValue += abs(oneGoal[0] - row)
                    HValue += abs(oneGoal[1] - col)
                elif value[row][col] == 2:
                    HValue += abs(twoGoal[0] - row)
                    HValue += abs(twoGoal[1] - col)
                elif value[row][col] == 3:
                    HValue += abs(threeGoal[0] - row)
                    HValue += abs(threeGoal[1] - col)
                elif value[row][col] == 4:
                    HValue += abs(fourGoal[0] - row)
                    HValue += abs(fourGoal[1] - col)
                elif value[row][col] == 5:
                    HValue += abs(fiveGoal[0] - row)
                    HValue += abs(fiveGoal[1] - col)
                elif value[row][col] == 6:
                    HValue += abs(sixGoal[0] - row)
                    HValue += abs(sixGoal[1] - col)
                elif value[row][col] == 7:
                    HValue += abs(sevenGoal[0] - row)
                    HValue += abs(sevenGoal[1] - col)
                elif value[row][col] == 8:
                    HValue += abs(eightGoal[0] - row)
                    HValue += abs(eightGoal[1] - col)
        FValue = state.g + HValue
        state.f = FValue
        if(len(queue)) == 0: #if the queue is empty, just insert it into front
            queue.append(state)
        else:
            valueInserted = False
            for i in range(len(queue)): #iterate through the queue, put potential move into queue based on F value
                if(queue[i].f >= FValue): #if the current value in queue has an F value greater than the F value of the potential action we are looking at
                    queue.insert((i), state)
                    valueInserted = True 
                    break
            if(valueInserted == False): #if no other F value is greater than current value, put on end
                queue.append(state)
    return(queue)

# def possibleActions(currentState, alreadyTraveledStates, Gvalue)
# given the current Node and a list of already already travelled states, will determine
# other potential moves that can be made

# Parameters:
# currentState - the Node we want to branch out from
# alreadyTraveledStates - a list of nodes already explored
# G value that will be assigned to any created nodes 

# Returns:
# list of new Nodes that will later be sorted by sortQueueUsingManhattan()

def possibleActions(currentState, alreadyTraveledStates, Gvalue):
    currentStateValue = currentState.value #grab the 2d array value from the node
    possibleActionsList = []
    NewZeroLocations = []
    directionTravelled = []
    ZeroRow = -1 
    ZeroCol = -1
    for row in range(3):  #find where the empty tile is
        for col in range(3):
            if currentStateValue[row][col] == 0:
                ZeroRow = row
                ZeroCol = col

    
    moveZeroUp = [ZeroRow -1, ZeroCol] #coords of the empty stone if it moved up
    moveZeroDown = [ZeroRow + 1, ZeroCol] #coords of the empty stone if it moved down
    moveZeroRight = [ZeroRow, ZeroCol + 1] #coords of the empty stone if it moved right
    moveZeroLeft = [ZeroRow, ZeroCol - 1] #coords of the empty stone if it moved left

    #boundary check, if in bounds, add to a list
    if(moveZeroUp[0] > -1):
        NewZeroLocations.append(moveZeroUp)
        directionTravelled.append("up")
    if(moveZeroDown[0] < 3):
        NewZeroLocations.append(moveZeroDown)
        directionTravelled.append("down")
    if(moveZeroRight[1] < 3):
        NewZeroLocations.append(moveZeroRight)
        directionTravelled.append("right")
    if(moveZeroLeft[1] > -1):
        NewZeroLocations.append(moveZeroLeft)
        directionTravelled.append("left")
    #these are the places the empty stone can move
    #for each of these options, we will find what the new board state is
    for option in NewZeroLocations:
        possibleActionTemp = copy.deepcopy(currentStateValue)  #giving same address 
        temp = currentStateValue[option[0]][option[1]] #get value that is to be swapped with 0
        possibleActionTemp[option[0]][option[1]] = 0 #put zero into that spot
        possibleActionTemp[ZeroRow][ZeroCol] = temp #put the temporary value into the zero position
        duplicateFound = False
        for i in range(len(alreadyTraveledStates)): #make sure this state has not already been explored
            if(alreadyTraveledStates[i].value == possibleActionTemp):
                duplicateFound = True
        if(duplicateFound == True):
            if(len(directionTravelled) > 0):
                    directionTravelled.pop(0) #we want to make sure the node we create has the right direction, if a duplicate is found, we have to pop its direction too
            continue
        else:
             possibleActionsList.append(Node(possibleActionTemp, Gvalue, currentState, directionTravelled.pop(0))) #duplicate found, make a new Node 
    
    return(possibleActionsList) #return list of Nodes with new states

#program runs infinitely as of right now... manually terminate to stop
while True:
    initializeBoard()
