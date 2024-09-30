#//  tic-tac-toe.py
#//  Tic Tac Toe
#//
#//  Created by Sinmisola Kareem on 9/30/24.
#//

class TicTacToe:
    def __init__(self):
        # Initialize the game board with 9 empty spaces
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        # Print the current state of the game board
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
        print(f"Current player: {self.current_player}")

    def has_won(self, player):
        winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1,4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        return any(all(self.board[i] == player for i in combo) for combo in winning_combos)


    def is_draw(self):
        # Check if the game is a draw
        return ' ' not in self.board

    def ai_move(self):
        if self.has_won('X') or self.is_draw():
            return  # Game is already over, no need to make a move
        # Use the Minimax algorithm to determine the best move for the AI opponent
        best_score = float('-inf')
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = 'O'
        self.current_player = 'X'

    def minimax(self, board, depth, is_maximizing, memo={}):
        key = tuple(board)  # Create a unique key for the board state
        if key in memo:
            return memo[key]

        if self.has_won('O'):
            score = 10 - depth
        elif self.has_won('X'):
            score = depth - 10
        elif self.is_draw():
            score = 0
        else:
            if is_maximizing:
                best_score = float('-inf')
                for i in range(9):
                    if board[i] == ' ':
                        board[i] = 'O'
                        score = self.minimax(board, depth + 1, False, memo)
                        board[i] = ' '
                        best_score = max(score, best_score)
            else:
                best_score = float('inf')
                for i in range(9):
                    if board[i] == ' ':
                        board[i] = 'X'
                        score = self.minimax(board, depth + 1, True, memo)
                        board[i] = ' '
                        best_score = min(score, best_score)
            score = best_score

        memo[key] = score
        return score


    def get_move(self, player):
        while True:
            move = input(f"Player {player}, enter your move (1-9): ")
            if move.isdigit() and 1 <= int(move) <= 9 and self.board[int(move) - 1] == ' ':
                self.board[int(move) - 1] = player
                self.current_player = 'O' if player == 'X' else 'X'  # Toggle current player
                break
            else:
                print("Invalid move, try again.")


    def play_game(self):
        # Play the game with the AI opponent
        while True:
            self.print_board()
            self.get_move(self.current_player)
            if self.has_won(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            elif self.is_draw():
                self.print_board()
                print("It's a draw!")
                break
            self.ai_move()
            if self.has_won('O'):
                self.print_board()
                print("AI wins!")
                break

def main():
    game = TicTacToe()
    game.play_game()

if __name__ == "__main__":
    main()
