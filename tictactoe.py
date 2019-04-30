from random import randint

class TicTacToe:
    def __init__(self):
        print("Legend:")
        self.__board = [str(i) for i in range(1, 10)]
        self.drawBoard()
    
    def __playerMove(self):
        while True:
            while True:
                try:
                    move = int(input("Player {0}\'s move: ".format(self.__turn + 1)))
                except ValueError:
                    print("Input was not a number.")
                    continue

                if move not in range(1, 10):
                    print("Invalid space.")
                else:
                    move-=1
                    break

            if self.__board[move] == ' ':
                if self.__turn == 0:
                    self.__board[move] = self.player1
                else:
                    self.__board[move] = self.player2

                return move
            else:
                print("Space already taken.")

    def __computerMove(self):
        if self.__firstMove:
            move = randint(0, 8)
            self.__firstMove = False
        else:
            score = -362881

            for i in range(9):
                if self.__board[i] == ' ':
                    currBoard = self.__board[:]
                    currBoard[i] = self.player2

                    if self.isWin(currBoard, i):
                        move = i
                        break

                    tmp = self.__bestMove(currBoard, not self.__turn)

                    if tmp > score:
                        score = tmp
                        move = i

        print("Computer's move: {0}".format(move + 1))
        self.__board[move] = self.player2
        return move

    def __bestMove(self, board, turn):
        score = 0

        for i in range(9):
            if board[i] == ' ':
                currBoard = board[:]

                if turn == 0:
                    currBoard[i] = self.player1

                    if self.isWin(currBoard, i):
                        return -1
                else:
                    currBoard[i] = self.player2

                    if self.isWin(currBoard, i):
                        return 1

                score += self.__bestMove(currBoard, not turn)
                    
        return score

    def isWin(self, board, lastMove):
        row = lastMove // 3
        column = lastMove % 3

        return ((board[row * 3] == board[row * 3 + 1]
                and board[row * 3] == board[row * 3 + 2])                                         # equal row
            or (board[row * 3 + column] == board[(row + 1) % 3 * 3 + column]
                and board[row * 3 + column] == board[(row + 2) % 3 * 3 + column])                 # equal column
            or (row == column
                and board[row * 3 + column] == board[(row + 1) % 3 * 3 + (column + 1) % 3]
                and board[row * 3 + column] == board[(row + 2) % 3 * 3 + (column + 2) % 3])       # equal diagonal
            or (row + column == 2
                and board[row * 3 + column] == board[(row + 2) % 3 * 3 + (column + 1) % 3]
                and board[row * 3 + column] == board[(row + 1) % 3 * 3 + (column + 2) % 3]))      # equal anti-diagonal

    def drawBoard(self):
        for i in range(4, -1, -1):
            if i % 2 == 0:
                print(self.__board[i//2*3] + '|' + self.__board[i//2*3 + 1] + '|' + self.__board[i//2*3 + 2])
            else:
                print('\u2014 ' * 3)

        print('\n')

    def play(self, players):
        self.__board = [' ' for i in range(9)]

        while True:
            self.player1 = input("Player 1, X or O: ").strip().upper()

            if self.player1 not in ('X', 'O'):
                print("Invalid input.")
            else:
                if self.player1 == 'X':
                    self.player2 = 'O'
                    self.__turn = 0
                else:
                    self.player2 = 'X'
                    self.__turn = 1

                break

        print("\nPlayer 1: {0}".format(self.player1))

        if players == 1:
            print("Computer: {0}\n".format(self.player2))
            self.__firstMove = bool(self.__turn)
            
            if self.__turn == 0:
                self.drawBoard()

            for _ in range(9):
                if self.__turn == 0:
                    move = self.__playerMove()
                else:
                    move = self.__computerMove()

                self.drawBoard()
                
                if self.isWin(self.__board, move):
                    if self.__turn == 0:
                        print("Game over. You win!")
                    else:
                        print("Game over. I win!")

                    return

                self.__turn = not self.__turn
        else:
            print("Player 2: {0}\n".format(self.player2))
            self.drawBoard()

            for _ in range(9):
                move = self.__playerMove()
                self.drawBoard()
                
                if self.isWin(self.__board, move):
                    print("Game over. Player {0} wins!".format(self.__turn + 1))
                    return

                self.__turn = not self.__turn

        print("Game over. It's a tie!")

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