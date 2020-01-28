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
    pass

def compMove(pos, board):
    pass

def start():
    print("Welcome to the Tic-Tac-Toe game!")
    print("Please select what mode would you like to play (1 or 2):")
    print("(1) - Player vs Computer")
    print("(2) - Player vs Player")
    game = input(">>> ")
    print(type(game))
    while game != "1" or game != "2":
        print("Incorrect input. Please select mode 1 or 2:")
        print("(1) - Player vs Computer")
        print("(2) - Player vs Player")
        game = input(">>> ")

    if(game == "1"): #TODO AI
        pass
    if(game == "2"):
        print("Starting game Player vs Player!")
        print("Good luck and have fun!")
        print("")
        print("Player X It's your turn! (Select position 1-9 starting from top left)")
        printBoard(board)
        move = input(">>> ")
        try:
            move = int(move)
        except:
            print("Please select position from 1-9 starting from top left")


start()