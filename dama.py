import random, time
from sys import argv

PL1 = 'Player One'
PL2 = 'Player Two'
class Board:
    
# part 1 of the progam( building the board and the pieces)

    def __init__(self, row, column, skipRule = False):
        self.board = [[ 0 for c in range (column + 1)] for i in range (row + 1)]
        self.SetPlayerOne()
        self.SetPlayerTwo()

        self.printHelper()
        if not skipRule:
           self.printRules()
        self.scores = {
            
        }
        self.turn = 0
        self.playerTurn = ''
        self.scoreCount = 0
        
    def printBoard(self):
        for i in self.board:
            for j in i:
                print(j,end = " ")
            print()
    
    def printHelper(self):
        for j in range(7):
            self.board[0][j] = j
        for i in range(9):
            self.board[i][0] = i
        self.board[0][0] = '+'

    def SetPlayerOne(self):
        
        for i in range(1, 4):
            for j in range(1,7):
                if (i == 1 or i == 3) and (j%2==0):
                    self.board[i][j] = '*'
                elif i == 2 and j % 2 == 1:
                    self.board[i][j] = "*"
                else:
                    continue
        self.nonplayablePositions()
    def nonplayablePositions(self):
        
        for i in range(4, 6):
            for j in range(1,7):
                if i == 4 and j % 2 == 1:
                    self.board[i][j] = ' '
                elif i == 5  and j %2 == 0:
                    self.board[i][j] = ' '
                else:
                    continue
                
    def SetPlayerTwo (self):
        for i in range(6,9):
            for j in range(1,7):
                if (i == 6 or i  == 8) and j%2==1 :
                    self.board[i][j]='#'
                elif i ==7 and j % 2 == 0:
                    self.board[i][j]="#"
                else:
                    continue
    
    def printRules(self):
            print('Before starting the game, Let us look at some basic rules of the game\n')
            time.sleep(2)
            print('To move the Pieces: ')
            time.sleep(2)
            print(f"Enter the index of the pieces you want to move and where you want to move it. First select the index of the cooridante you want to me. Suppose you want to move a piece located at row 3 column 2, you should input '3,2'.\n")
            time.sleep(4)
            print("Then select the index of where you want to move the piece. Suppose you want to move a piece to row 4 column 1, you should input '4,1'")
            time.sleep(6)
            print('The game will end when either of the players have no moves to make or do not have any piece to move')
            time.sleep(3)
            print('Let us start the game')
            time.sleep(3)

   # Part 2 of the program. Implementing th movments of the program.  
    def Move(self, rowOld, columnOld, rowNew, columnNew, Error= False):
        if self.playerTurn == 'Player One':
            self.playerOneMove(rowOld,columnOld,rowNew,columnNew)
        elif self.playerTurn== 'Player Two':
            self.playerTwoMove(rowOld,columnOld,rowNew,columnNew)
            
    def isPlayerOneMoveValid(self, rowOld, columnOld, rowNew, columnNew):
        if(self.board[rowOld][columnOld] != self.board[rowNew][columnNew] and rowNew == rowOld + 1 and rowNew != 0 and self.board[rowOld][columnOld]=="*" and columnNew != 0):
            return True
        return False
    
    def isPlayerOneTakePiece(self, rowOld, columnOld, rowNew, columnNew):
        if (self.board[rowOld][columnOld]=='*' and self.board[rowNew][columnNew]=='#'):
            return True
        else:
            return False

    def playerOneMove(self,rO, cO, rN, cN, Error = False ):
        if Error == False:
            if(self.isPlayerOneMoveValid(rO,cO,rN,cN)):
                if (self.isPlayerOneTakePiece(rO,cO,rN,cN)):     
                    self.takePiece(rO, cO, rN, cN) 
                elif (cO > 1 and (self.isMovingRight(cO, cN) or self.isMovingLeft(cO, cN)  and self.board[rN][cN]!='#' )):
                    self.move(rO, cO, rN, cN)
                elif( cO == 1 and cN == cO + 1 and self.board[rN][cN]!='#'):
                    self.move(rO, cO, rN, cN)
                else:
                    print('Player 1: Voilating move')
                    list= self.inputCordinates() 
                    self.playerOneMove(list[0], list[1], list[2], list[3])             
            else:
                print('Player 1: Voilating move')
                list= self.inputCordinates() 
                self.playerOneMove(list[0], list[1], list[2], list[3])
        else:
            print('Please enter the right input with the correct format: ')
            list = self.inputCordinates()
            self.playerOneMove(list[0], list[1], list[2], list[3], list[4])
                
    def choosePlayer(self, rO, cO):
        if(self.board[rO][cO]== "*"):
            list= self.inputCordinates() 
            self.playerOneMove(list[0], list[1], list[2], list[3])
        elif(self.board[rO][cO]== "#"):
            list= self.inputCordinates() 
            self.playerTwoMove(list[0], list[1], list[2], list[3])

    def playerTwoMove(self,rO, cO, rN, cN, Error = False):
        if Error == False and (rO, rN < 9) and (cO,cN < 7):
            if(self.board[rO][cO] != self.board[rN][cN] and rO == rN + 1 and self.board[rO][cO]=="#" ):
                #                  right           left
                if (cO > 1 and (self.isMovingRight(cO,cN) or self.isMovingLeft(cO , cN)) and self.board[rN][cN]!='*' ):
                    self.move(rO, cO, rN, cN)
                #                     left 
                elif( cO == 1 and self.isMovingRight(cO,cN) and self.board[rN][cN]!='*' ):
                    self.move(rO, cO, rN, cN)
                elif(self.board[rO][cO]=='#' and self.board[rN][cN]=='*'):
                    self.takePiece(rO, cO, rN, cN)
                else:
                    print('Player 2: Voilating move')
                    list= self.inputCordinates() 
                    self.playerTwoMove(list[0], list[1], list[2], list[3])
            else:
                print('Player 2: Voilating move')
                list= self.inputCordinates() 
                self.playerTwoMove(list[0], list[1], list[2], list[3])
        else:
            print('Please enter the right input with the correct format: ')
            list = self.inputCordinates()
            self.playerTwoMove(list[0], list[1], list[2], list[3], list[4])

    # pass player parameter here 
    def isMovingLeft(self, columnOld, columnNew):
        if (columnNew == columnOld - 1):
            return True
    def isMovingRight(self, columnOld, columnNew):
        if( columnNew == columnOld +1 ):
            return True
            
    def takePiece(self, rowOld, columnOld, rowNew, columnNew):
        if (self.playerTurn =="Player Two"):                     
            if self.isMovingLeft(columnOld, columnNew) :
                if(self.board[rowNew-1][columnNew-1]== " "):
                    self.board[rowNew][columnNew] = " "
                    self.move(rowOld,columnOld,rowNew-1, columnNew-1)
                    self.score(self.playerTurn)
                else:
                    print('Violating move')
                    self.choosePlayer(rowOld, columnOld)
            elif self.isMovingRight(columnOld, columnNew):
                if(self.board[rowNew-1][columnNew+1]== " "):
                    self.board[rowNew][columnNew] = " "
                    self.move(rowOld,columnOld,rowNew-1, columnNew+1)
                    self.score(self.playerTurn)
                else:
                    print('Violating move')
                    self.choosePlayer(rowOld, columnOld)
        elif(self.playerTurn == "Player One"):
            if (self.isMovingLeft(columnOld , columnNew)):
                if(self.board[rowNew+1][columnNew-1]== " "):
                    self.board[rowNew][columnNew] = " "
                    self.move(rowOld,columnOld,rowNew+1, columnNew-1)
                    self.score(self.playerTurn)
                else:
                    print("Violating move")
                    self.choosePlayer(rowOld, columnOld)
            elif(self.isMovingRight(columnOld, columnNew) ):
                if(self.board[rowNew+1][columnNew+1]== " "):
                    self.board[rowNew][columnNew] = " "
                    self.move(rowOld,columnOld,rowNew+1, columnNew+1)
                    self.score(self.playerTurn)
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
    
    def turnKepper(self):
        if( self.turn % 2==0):
            print("Player One's turn")
            self.playerTurn = 'Player One'

        elif(self.turn % 2 == 1):
            print("Player Two's turn")
            self.playerTurn = 'Player Two'
        else:
            return 1
        self.turn= self.turn + 1

# part 3 of the program(playing the game)

    def play(self):
        startTime = endTime = time.time()
        value = ""
        print("To quit the game press Q. To continue to the game press Enter")
        value = input()
        while(value.lower() != 'q'):
            self.turnKepper()
            list = self.inputCordinates()
            self.Move(list[0], list[1], list[2], list[3], list[4])
            self.printBoard()
            if self.scoreCount == 9:
                break
        for i in self.scores:
            if self.scores[i] == self.scoreCount:
                print(f"{i} WINS!!!")

        totalTime = time.time() - startTime
        print("Game completed in ", round(totalTime, 2) , "seconds")
        
    def inputCordinates(self):
        # use camelCase convention
        Error = False        
        Oldinput = input(" Enter the indices of the piece you wish to move: ")
        Newinput = input("Enter the indices of the the place you want your piece to move: ")
        columnOld, rowOld, rowNew, columnNew = 0, 0, 0, 0
        try:
            columnOld = int(Oldinput.split(',')[1])
            rowOld = int(Oldinput.split(',')[0])
            columnNew = int(Newinput.split(',')[1])
            rowNew = int(Newinput.split(',')[0])
        except IndexError:
            Error = True
        except ValueError:
            Error = True
        return ( rowOld,  columnOld, rowNew, columnNew, Error )

    def score(self,turn):

        if turn in self.scores:
            self.scores[turn] += 1
            print(self.scores)
        else:
            self.scores[turn] = 1
        self.scoreCount = max(self.scores.values())

game = None
if len(argv) > 1 and argv[1] == 'skip-rules':
    game = Board(8, 6, True)
else:
    game = Board(8,6)
game.printBoard()
game.play()
