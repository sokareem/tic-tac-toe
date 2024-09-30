# Tic Tac Toe Game Documentation

## Overview
The Tic Tac Toe game is a classic two-player strategy game where players, X and O, compete to place their symbols in a 3x3 grid. The game is implemented in Python using object-oriented programming, with a simple graphical user interface (GUI) for player interaction.

## Gameplay

### Game Board
- The game board is a 3x3 grid, represented by a list of 9 elements.
- The board is initialized with empty spaces, represented by `' '`.

### Game Rules
- Player X makes the first move.
- Players take turns entering a number (1-9) to place their symbol in the corresponding position on the board.
- A player can only place their symbol on an empty space.
- The game ends when:
  - A player has three symbols in a row (horizontally, vertically, or diagonally).
  - The board is full, resulting in a draw.

### AI Opponent
- The game includes an AI opponent that uses the **Minimax algorithm** to make the best possible move.

### Game States
- **Not Started**: The game hasn't started; no moves have been made.
- **In Progress**: The game is ongoing, and players are making moves.
- **Won**: A player has won the game by aligning three symbols.
- **Draw**: The game ends in a draw, with no winner.

## API Endpoints

### `__init__`
- Initializes a new game instance.
- **Parameters**: None
- **Returns**: None

### `print_board`
- Prints the current state of the game board.
- **Parameters**: None
- **Returns**: None

### `has_won`
- Checks if a player has won the game.
- **Parameters**:
  - `player` (str): The player to check (either 'X' or 'O').
- **Returns**: `bool` - `True` if the player has won, `False` otherwise.

### `is_draw`
- Checks if the game has ended in a draw.
- **Parameters**: None
- **Returns**: `bool` - `True` if the game is a draw, `False` otherwise.

### `ai_move`
- Makes a move for the AI opponent using the Minimax algorithm.
- **Parameters**: None
- **Returns**: None

### `get_move`
- Gets the move from the current player.
- **Parameters**:
  - `player` (str): The player to get the move from ('X' or 'O').
- **Returns**: `int` - The move made by the player.

### `play_game`
- Plays the game against the AI opponent.
- **Parameters**: None
- **Returns**: None

### `minimax`
- Calculates the best score for a given board state using the Minimax algorithm.
- **Parameters**:
  - `board` (list): The current state of the game board.
  - `depth` (int): The current depth of the game tree.
  - `is_maximizing` (bool): Whether this is the maximizing player's turn.
  - `memo` (dict): A dictionary to store scores for previously visited board states.
- **Returns**: `int` - The best score for the given board state.

## Usage

To play the game, create a new instance of the `TicTacToe` class and call the `play_game` method.

### Example: Playing the Game
```python
game = TicTacToe()
game.play_game()
```

### Example: Getting a Player's Move
```python
game = TicTacToe()
game.current_player = 'X'
move = game.get_move('X')
print(move)
```

### Example: Printing the Game Board
```python
game = TicTacToe()
game.print_board()
```

## Troubleshooting

### Invalid Move
- If a player enters an invalid move, the game will print an error message and prompt the player to enter a valid move.

### AI Opponent Not Moving
- Ensure that the game board isn't full and the AI hasn't already won the game.

## Commit Messages
When committing changes, use the following format:
```
"Fixed bug in AI opponent logic"
```

## Code Quality
The code follows object-oriented programming principles and is well-documented, with clear comments explaining each method.

## Testing
The game includes unit tests to ensure the game logic functions correctly. Tests cover:
- Valid and invalid moves.
- AI opponent making a move.
- Game ending in a win or a draw.

Tests are written using the `unittest` framework.

## Security
The code is secure and follows good coding practices. No security vulnerabilities are present.

## Requirements
- Python 3.x is required to run the game.
- **Dependencies**: Install the game’s dependencies using `pip`.

## Installation
To install the game, run:
```bash
pip install .
```

## Running the Code
To start the game, run:
```bash
python -m tic_tac_toe
```

---
