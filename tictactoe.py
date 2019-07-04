from random import randint


class TicTacToe:
    def __init__(self):
        self.player1 = 'X'
        self.player2 = 'O'
        self._turn = 0
        self._computer_first_move = False
        self._board = [str(i) for i in range(1, 10)]
        print("Legend:")
        self.draw_board()

    def draw_board(self):
        for i in range(4, -1, -1):
            if i % 2 == 0:
                print(self._board[i // 2 * 3] + '|' + self._board[i // 2 * 3 + 1] + '|' + self._board[i // 2 * 3 + 2])
            else:
                print('\u2014 ' * 3)

        print('\n')

    def play(self, players):
        self._board = [' ' for i in range(9)]

        while True:
            self.player1 = input("Player 1, X or O: ").strip().upper()

            if self.player1 not in ('X', 'O'):
                print("Invalid input.")
            else:
                if self.player1 == 'X':
                    self.player2 = 'O'
                    self._turn = 0
                else:
                    self.player2 = 'X'
                    self._turn = 1

                break

        print(f"\nPlayer 1: {self.player1}")

        if players == 1:
            print(f"Computer: {self.player2}\n")
            self._computer_first_move = bool(self._turn)
            
            if self._turn == 0:
                self.draw_board()

            for _ in range(9):
                if self._turn == 0:
                    move = self._player_move()
                else:
                    move = self._computer_move()

                self.draw_board()
                
                if self._is_win(self._board, move):
                    if self._turn == 0:
                        print("Game over. You win!")
                    else:
                        print("Game over. I win!")

                    return

                self._turn = not self._turn
        else:
            print(f"Player 2: {self.player2}\n")
            self.draw_board()

            for _ in range(9):
                move = self._player_move()
                self.draw_board()
                
                if self._is_win(self._board, move):
                    print(f"Game over. Player {self._turn + 1} wins!")
                    return

                self._turn = not self._turn

        print("Game over. It's a tie!")

    def _player_move(self):
        while True:
            while True:
                try:
                    move = int(input(f"Player {self._turn + 1}'s move: "))
                except ValueError:
                    print("Input was not a number.")
                    continue

                if move not in range(1, 10):
                    print("Invalid space.")
                else:
                    move -= 1
                    break

            if self._board[move] == ' ':
                if self._turn == 0:
                    self._board[move] = self.player1
                else:
                    self._board[move] = self.player2

                return move
            else:
                print("Space already taken.")

    def _computer_move(self):
        if self._computer_first_move:
            move = randint(0, 8)
            self._computer_first_move = False
        else:
            max_score = -362881

            for i in range(9):
                if self._board[i] == ' ':
                    curr_board = self._board[:]
                    curr_board[i] = self.player2

                    if self._is_win(curr_board, i):
                        move = i
                        break

                    score, min_loss_depth = self._best_move(curr_board, not self._turn, 1)

                    if score > max_score and min_loss_depth != 1:
                        move = i
                        max_score = score

        print(f"Computer's move: {move + 1}")
        self._board[move] = self.player2
        return move

    def _best_move(self, board, turn, depth):
        score = 0
        min_loss_depth = 9

        for i in range(9):
            if board[i] == ' ':
                curr_board = board[:]

                if turn == 0:
                    curr_board[i] = self.player1

                    if self._is_win(curr_board, i):
                        return -1, depth
                else:
                    curr_board[i] = self.player2

                    if self._is_win(curr_board, i):
                        return 1, 9

                tmp_score, loss_depth = self._best_move(curr_board, not turn, depth + 1)
                score += tmp_score

                if loss_depth < min_loss_depth:
                    min_loss_depth = loss_depth

        return score, min_loss_depth

    @staticmethod  # can be used by _best_move()
    def _is_win(board, last_move):
        row = last_move // 3
        column = last_move % 3

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


if __name__ == "__main__":
    print("Playing Tic-Tac-Toe")
    game = TicTacToe()
    play = True
    
    while play:
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
