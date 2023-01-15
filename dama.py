import random, time
class Board:
    
# part 1 of the progam( building the board and the pieces)

    def __init__(self, row, column):
        self.board = self.board = [[ 0 for c in range (column)] for i in range (row)]
        self.playerOne()
        self.playerTwo()

    def printBoard(self):
        for i in self.board:
            for j in i:
                print(j,end = " ")
            print()

    def playerOne(self):
        for i in range(3):
            for j in range(0,6):
                if i == 0:
                    if j%2==0:
                        self.board[i][j] = '*'
                elif i == 1:
                    if j %2 == 1:
                        self.board[i][j] = "*"
                elif i ==2:
                    if j%2 == 0:
                        self.board[i][j] = "*"
                else:
                    continue
        self.nonplayablePositions()
    def nonplayablePositions(self):
        for i in range(3, 5):
            for j in range(0,6):
                if i == 3:
                    if j%2==1:
                        self.board[i][j] = ' '
                elif i == 4:
                    if j %2 == 0:
                        self.board[i][j] = ' '
                else:
                    continue
    def playerTwo (self):
        for i in range(5,8):
            for j in range(0,6):
                if i == 5:
                    if j%2==1:
                        self.board[i][j]='#'
                elif i ==6:
                    if j %2 == 0:
                        self.board[i][j]="#"
                elif i ==7:
                    if j%2==1:
                        self.board[i][j]="#"
                else:
                    continue
                
# part 2 of the program(implementing movments of the pieces)

    def playerOneMove(self,rO, cO, rN, cN):
        while(self.board[rO][cO] != self.board[rN][cN] and rN == rO + 1 and self.board[rO][cO]=="*" ):
            if (cO!= 0 and (cN == cO + 1 or cN == cO - 1)  and self.board[rN][cN]!='#' ):
                self.move(rO, cO, rN, cN)
            elif( cO == 0 and cN == cO + 1 and self.board[rN][cN]!='#'):
                self.move(rO, cO, rN, cN)
            elif(self.board[rO][cO]=='*' and self.board[rN][cN]=='#'):
                self.takePiece(rO, cO, rN, cN) 
            break
        else:
            print('Player 1: Voilating move')
            list= self.inputCordinates() 
            self.playerOneMove(list[0], list[1], list[2], list[3])
            
    def choosePlayer(self, rO, cO):
        if(self.board[rO][cO]== "*"):
            list= self.inputCordinates() 
            self.playerOneMove(list[0], list[1], list[2], list[3])
        elif(self.board[rO][cO]== "#"):
            list= self.inputCordinates() 
            self.playerTwoMove(list[0], list[1], list[2], list[3])

    def playerTwoMove(self,rO, cO, rN, cN):
        while(self.board[rO][cO] != self.board[rN][cN] and rO == rN + 1 and self.board[rO][cO]=="#" ):
            if (cO!= 0 and (cN == cO + 1 or cN == cO - 1) and self.board[rN][cN]!='*' ):
                self.move(rO, cO, rN, cN)
            elif( cO == 0 and cN == cO + 1 and self.board[rN][cN]!='*' ):
                self.move(rO, cO, rN, cN)
            elif(self.board[rO][cO]=='#' and self.board[rN][cN]=='*'):
                self.takePiece(rO, cO, rN, cN)
                #self.switcher(rO, cO, rN, cN)
            break
        else:
            print('Player 2: Voilating move')
            list= self.inputCordinates() 
            self.playerTwoMove(list[0], list[1], list[2], list[3])
    
    '''    def switcher(self, rowOld, columnOld, rowNew, columnNew):
        switcher ={
            rowNew==rowOld-1: self.takePiece,
            rowNew==rowOld+1: self.takePiece,
        }
        return switcher.get(rowOld, columnOld, rowNew, columnNew)
'''

    def takePiece(self, rowOld, columnOld, rowNew, columnNew):
        if(rowNew== rowOld - 1):
            if (columnNew == columnOld - 1):
                while(self.board[rowNew-1][columnNew-1]== " "):
                    self.board[rowNew][columnNew] = " "
                    self.move(rowOld,columnOld,rowNew-1, columnNew-1)
                    break
                else:
                    print('Violating move')
                    self.choosePlayer(rowOld, columnOld)
            elif( columnNew== columnOld +1 ):
                while(self.board[rowNew-1][columnNew+1]== " "):
                    self.board[rowNew][columnNew] = " "
                    self.move(rowOld,columnOld,rowNew-1, columnNew+1)
                    break
                else:
                    print('Violating move')
                    self.choosePlayer(rowOld, columnOld)
        elif(rowNew == rowOld + 1):
            if (columnNew == columnOld - 1):
                while(self.board[rowNew+1][columnNew-1]== " "):
                    self.board[rowNew][columnNew] = " "
                    self.move(rowOld,columnOld,rowNew-1, columnNew-1)
                    break
                else:
                    print("Violating move")
                    self.choosePlayer(rowOld, columnOld)
            elif( columnNew== columnOld +1 ):
                while(self.board[rowNew+1][columnNew+1]== " "):
                    self.board[rowNew][columnNew] = " "
                    self.move(rowOld,columnOld,rowNew-1, columnNew+1)
                    break
                else:
                    print("Violating move")
                    self.choosePlayer(rowOld, columnOld)          

    def move(self, rowOld, columnOld, rowNew,columnNew):
        piece = self.selectPiece(rowOld, columnOld, rowNew, columnNew)
        newPosition = self.movePiece(piece, rowNew, columnNew)
        
    def movePiece(self, piece, r, c):
        self.board[r][c] = piece
        return self.board[r][c]
    
    def selectPiece(self, rowO, columnO, rowN, columnN):
        a=  self.board[rowO][columnO]
        self.board[rowO][columnO]= self.board[rowN][columnN]
        return a
    turn = 0
    def turnKepper(self):
        if( self.turn % 2==0):
            print("Player One's turn")
        elif(self.turn % 2 == 1):
            print("Player Two's turn")
        else:
            return 1
        self.turn=self.turn + 1

# part 3 of the program(playing the game)
    
    def play(self):
        startTime = time.time()
        endTime = startTime
        value = ""
        print("To quit the game press Q. To continue to the game press Enter")
        value= input()
        while(value.lower() != 'q'):
            self.turnKepper()
            list = self.inputCordinates()
            self.playerOneMove(list[0], list[1], list[2], list[3])
            self.printBoard()
            self.turnKepper()
            listTwo = self.inputCordinates()
            self.playerTwoMove(listTwo[0], listTwo[1], listTwo[2], listTwo[3])
            self.printBoard()
        totalTime = time.time() - startTime
        print("Game completed in ", round(totalTime, 2) , "seconds")
    def inputCordinates(self):
        rowOld = int(input("The row of the piece you want to move: "))
        columnOld = int(input("The column of the piece you want to move: "))
        rowNew = int(input("The row where you want your picece to move: "))
        columnNew = int(input("The column where you want your piece to move: "))
        return ( rowOld,  columnOld, rowNew, columnNew )
  
    
game= Board (8,6)
game.printBoard()
game.play()






'''
        ['w','.','w','.','w','.'],
        ['.','w','.','w','.','w'],
        ['w','.','w','.','w','.'],
        ['.',' ','.',' ','.',' '],
        [' ','.',' ','.',' ','.'],
        ['.','b','.','b','.','b'],
        ['b','.','b','.','b','.'],
        ['.','b','.','b','.','b']
'''
