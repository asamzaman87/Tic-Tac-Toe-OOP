# Tic Tac Toe Game
    # Board
        # keeping track of moves
        # determining winner
        # way for user to see what positions are available
        # check if filled in the case of a tie
    # Players
        # choosing the move
        # having a specific shape
        # getter method for shape

class Board:
    def __init__(self):
        self.board = []
        self.count = 0
        adder = []
        for i in range(9):
            if i % 3 == 0 and i != 0:
                self.board.append(adder)
                adder = []
            adder.append(i)
        self.board.append(adder)
                
    def __str__(self): 
        output = ''
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                output += str(self.board[row][col])
                if col == 0 or col == 1:
                    output += "|"
            if row == 0 or row == 1:
                output += "\n" + "-"*5 + "\n"
        return output + "\n"
        
    def update(self, number, player): 
        col, row = number % 3, number // 3
        if self.board[row][col] == "X" or self.board[row][col] == "O":
            raise Exception("Invalid position chosen!")
        else:
            self.board[row][col] = player.get_shape()
            self.count += 1
           
            
    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2]:
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return True

        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] or
                self.board[0][2] == self.board[1][1] == self.board[2][0]):
            return True

        return False
        
    def is_filled(self):
        return self.count == 9
            
class Player:
    def __init__(self, shape):
        self.shape = shape
        
    def get_shape(self):
        return self.shape
        
    def choose_move(self, number, board):
        if not (0 <= number <= 8):
            raise Exception("Invalid position chosen!")
        board.update(number, self)
    
    
##########################################################################
# Driver Code:
def handle_player_move(player, board, num):
    while True:
        pos = int(input(f"Player {num}, choose a position: "))
        try:
            player.choose_move(pos, board)
            break
        except Exception as e:
            print(str(e))

def play_game():
    board = Board()
    p1 = Player("X")
    p2 = Player("O")
    turn = True  # Player 1's turn

    while True:
        print(board)

        if turn:
            handle_player_move(p1, board, 1)
            turn = False
        else:
            handle_player_move(p2, board, 2)
            turn = True

        if board.check_winner():
            print(board)
            if turn:
                print("Player 2 is the winner!")
            else:
                print("Player 1 is the winner!")
            break

        if board.is_filled():
            print(board)
            print("The game is a tie!")
            break

play_game()

    
    
    
    
    

