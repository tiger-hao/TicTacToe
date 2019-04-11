class TicTacToe:
    def __init__(self):
        print("Legend:")
        self.board = [str(i) for i in range(1, 10)]
        self.drawBoard()

    def drawBoard(self):
        for i in range(4, -1, -1):
            if i % 2 == 0:
                print(self.board[i//2*3] + '|' + self.board[i//2*3 + 1] + '|' + self.board[i//2*3 + 2])
            else:
                print('\u2014 ' * 3)

        print('\n')

    def isWin(self, lastMove):
        row = lastMove // 3
        column = lastMove % 3

        return ((self.board[row * 3] == self.board[row * 3 + 1]
                and self.board[row * 3] == self.board[row * 3 + 2])                                         # equal row
            or (self.board[row * 3 + column] == self.board[(row + 1) % 3 * 3 + column]
                and self.board[row * 3 + column] == self.board[(row + 2) % 3 * 3 + column])                 # equal column
            or (row == column
                and self.board[row * 3 + column] == self.board[(row + 1) % 3 * 3 + (column + 1) % 3]
                and self.board[row * 3 + column] == self.board[(row + 2) % 3 * 3 + (column + 2) % 3])       # equal diagonal
            or (row + column == 2
                and self.board[row * 3 + column] == self.board[(row + 2) % 3 * 3 + (column + 1) % 3]
                and self.board[row * 3 + column] == self.board[(row + 1) % 3 * 3 + (column + 2) % 3]))      # equal anti-diagonal

    def play(self, players):
        self.board = [' ' for i in range(9)]

        while True:
            self.player1 = input("Player 1, X or O: ").strip().upper()

            if self.player1 not in ('X', 'O'):
                print("Invalid input.")
            else:
                if self.player1 == 'X':
                    self.player2 = 'O'
                    self.turn = 0
                else:
                    self.player2 = 'X'
                    self.turn = 1

                break

        print("\nPlayer 1: {0}".format(self.player1))

        if players == 1:
            print("Computer: {0}\n".format(self.player2))
            self.drawBoard()

            for _ in range(9):
                if self.turn == 0:
                    move = self.playerMove()
                else:
                    move = self.computerMove()

                self.drawBoard()
                
                if self.isWin(move):
                    if self.turn == 0:
                        print("Game over. You win!")
                    else:
                        print("Game over. I win!")

                    return

                self.turn = not self.turn
        else:
            print("Player 2: {0}\n".format(self.player2))
            self.drawBoard()

            for _ in range(9):
                move = self.playerMove()
                self.drawBoard()
                
                if self.isWin(move):
                    print("Game over. Player {0} wins!".format(self.turn + 1))
                    return

                self.turn = not self.turn

        print("Game over. It's a tie!")
    
    def playerMove(self):
        while True:
            while True:
                try:
                    space = int(input("Player {0}\'s move: ".format(self.turn + 1)))
                except ValueError:
                    print("Input was not a number.")
                    continue

                if space not in range(1, 10):
                    print("Invalid space.")
                else:
                    space-=1
                    break

            if self.board[space] not in ('X', 'O'):
                if self.turn == 0:
                    self.board[space] = self.player1
                else:
                    self.board[space] = self.player2

                return space
            else:
                print("Space already taken.")

    def computerMove(self):
        print("Computer's move:", "temp")
        return 0    # return space

if __name__ == "__main__":
    print("Playing Tic-Tac-Toe")
    game = TicTacToe()
    play = True
    
    while play == True:
        while True:
            try:
                players = int(input("How many players? (1/2)\n"))
            except ValueError:
                print("Input was not a number.")
                continue

            if players not in (1, 2):
                print("Invalid number.")
            else:
                break
    
        game.play(players)

        # end of game
        while True:
            x = input("Would you like to play again? (y/n)\n").strip().lower()

            if x not in ('y', 'n'):
                print("Invalid input.")
            else:
                if x == 'n':
                    play = False
                break

    print("Exiting...")