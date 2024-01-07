import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for deez in range(3):
            row = []
            for nuts in range(3):
                row.append('-')
            self.board.append(row)

    def random_player_uno(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def winnning_player(self, player):
        win = None

        x = len(self.board)

        # for the win by row
        for lol in range(x):
            win = True
            for lmao in range(x):
                if self.board[lol][lmao] != player:
                    win = False
                    break
            if win:
                return win

        # for the win by column
        for lol in range(x):
            win = True
            for lmao in range(x):
                if self.board[lmao][lol] != player:
                    win = False
                    break
            if win:
                return win

        # for the win by diagonals
        win = True
        for lol in range(x):
            if self.board[lol][lol] != player:
                win = False
                break
        if win:
            return win


        win = True
        for lol in range(x):
            if self.board[lol][x - 1 - lol] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.random_player_uno() == 1 else '0'
        while True:
            print(f"Player {player} turn")

            self.show_board()
            # taking user's input
            row, col = list(map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking if the player won
            if self.winnning_player(player):
                print(f"Player {player} win the game!")
                break
            # checking if it's a tie
            if self.is_board_filled():
                print("It's a draw!")
                break
            player = self.swap_player_turn(player)
        print()
        self.show_board()


gametime = TicTacToe()
gametime.start()