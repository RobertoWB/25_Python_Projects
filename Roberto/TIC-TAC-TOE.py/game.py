class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # We will use a single list to rep 3x3 board
        self.current_winner = None # Keep track of winner

    def print_board(self):
        # This is just getting the rows 
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' |'.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc

    