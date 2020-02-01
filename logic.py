board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def printBoard(board):
    print("     |     |")
    print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3])
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6])
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9])
    print("     |     |")


def isWinner(xoro, board):
    if(board[1] == xoro and board[2] == xoro and board[3] == xoro or
        board[4] == xoro and board[5] == xoro and board[6] == xoro or
        board[7] == xoro and board[8] == xoro and board[9] == xoro or
        board[1] == xoro and board[4] == xoro and board[7] == xoro or
        board[2] == xoro and board[5] == xoro and board[8] == xoro or 
        board[3] == xoro and board[6] == xoro and board[9] == xoro or 
        board[1] == xoro and board[5] == xoro and board[9] == xoro or 
        board[3] == xoro and board[5] == xoro and board[7] == xoro):
        return True
    return False

def playerMove(pos, board):
    board[pos] = "X"

def xMove(pos, board):
    board[pos] = "X"

def oMove(pos, board):
    board[pos] = "O"

def compMove(pos, board):
    pass

def isEmpty(pos, board):
    return board[pos] == " "

def isBoardEmpty(board):
    return " " in board[1:]

def start():
    print("Welcome to the Tic-Tac-Toe game!")
    print("Please select what mode would you like to play (1 or 2):")
    print("(1) - Player vs Computer")
    print("(2) - Player vs Player")
    game = input(">>> ")
    while game != "1" and game != "2":
        print("Incorrect input. Please select mode 1 or 2:")
        print("(1) - Player vs Computer")
        print("(2) - Player vs Player")
        game = input(">>> ")

    if(game == "1"): #TODO AI
        startPvC()
    if(game == "2"):
        startPvP()


def startPvP():
    print("Starting game Player vs Player!")
    print("Good luck and have fun!")
    print("")
    printBoard(board)
    while True:
        print("Player X its your turn! Please select position in range 1-9")
        move = int(input(">>> "))
        while move<1 or move > 9:
            printBoard(board)
            print("Please select position in range 1-9")
            move = int(input(">>> "))
        while not isEmpty(move, board):
            printBoard(board)
            print("This position is already occupied. Try again.")
            move = int(input(">>> "))
        else:
            xMove(move, board)
            printBoard(board)
            if(isWinner("X", board)):
                print("Player X won the game!")
                break
            if(not isBoardEmpty(board)):
                print("Draw! Game over!")
                break

        print("Player O its your turn! Please select position in range 1-9")
        move = int(input(">>> "))
        while move<1 or move > 9:
            printBoard(board)
            print("Please select position in range 1-9")
            move = int(input(">>> "))
        while not isEmpty(move, board):
            printBoard(board)
            print("This position is already occupied. Try again.")
            move = int(input(">>> "))
        else:
            oMove(move, board)
            printBoard(board)
            if(isWinner("O", board)):
                print("Player O won the game!")
                break
            if(not isBoardEmpty(board)):
                print("Draw! Game over!")
                break



def startPvC():
    pass
            


start()