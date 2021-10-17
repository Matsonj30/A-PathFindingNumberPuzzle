def initializeBoard():
   board = []
   row = []
   boardInput =  input("Enter nine numbers")
   for number in range(18):
        #print(number)
        if number % 2 == 0:
            #print(boardInput[number])
            row.append(int(boardInput[number]))
            print(row)
        if len(row) == 3:
            board.append(row)
            row = []
   print(board)   
initializeBoard()

