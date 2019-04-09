class TicTacToe:
    board = [str(i) for i in range(1, 10)]
    spaces = 9

    def drawBoard(self):
        for i in range(4, -1, -1):
            if i % 2 == 0:
                print(self.board[i//2*3] + '|' + self.board[i//2*3 + 1] + '|' + self.board[i//2*3 + 2])
            else:
                print('\u2014 ' * 3)

        print('\n')

    def play(self):
        print("Legend:")
        self.drawBoard()
        self.board = [' ' for i in range(9)]

        while True:
            x = input("X or O: ").strip().upper()

            if x not in ('X', 'O'):
                print("Invalid input.")
            else:
                self.player = x

                if x == 'X':
                    self.computer = 'O'
                else:
                    self.computer = 'X'

                break

        while self.spaces > 0:
            self.playerMove()
            self.computerMove()
            self.drawBoard()
            self.spaces-=1
    
    def playerMove(self):
        while True:
            while True:
                try:
                    space = int(input("Your move: "))
                except ValueError:
                    print("Input was not a number.")
                    continue

                if space not in range(1, 10):
                    print("Invalid space.")
                else:
                    space-=1
                    break

            if self.board[space] not in ('X', 'O'):
                self.board[space] = self.player
                break
            else:
                print("Space already taken.")

    def computerMove(self):
        pass

if __name__ == "__main__":
    game = TicTacToe()
    play = True
    
    while play == True:
        game.play()

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