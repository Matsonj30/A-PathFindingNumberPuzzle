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
   printboard(board)


def printboard(board):
    for row in board:
        for value in row:
            if value == 0:
                print("  ", end='')
            else:
                print(str(value) + " ", end='')
        print("")

initializeBoard()

