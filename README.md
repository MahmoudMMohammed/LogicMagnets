# Logic Magnets Puzzle Game

The Logic Magnets Puzzle Game involves a grid-based board where various types of pieces interact according to specific movement rules. The main goal is to solve the puzzle by moving the pieces to achieve a specific arrangement.


## State Description

The board is represented as a grid where each cell can contain a piece. The pieces include:

- **Red Magnet:** Pulls Iron Pieces towards it.
- **Purple Magnet:** Pushes Iron Pieces away from it.
- **Iron Piece:** Can be pushed or pulled by magnets.

Each cell on the board can either be movable or non-movable, and certain cells are designated as solve cells which need to be occupied to solve the puzzle.

## Start State

The start state is defined by a configuration which includes:

- The size of the board.
- Positions of solve cells.
- Positions of non-movable cells.
- Initial positions of Red Magnet, Purple Magnet, and Iron Pieces.

Example configuration:

```json
{
        "_comment": "Level: 1",
        "size": 4,
        "solve_cells": [[1, 1], [1, 3]],
        "non_movable_cells": [
            [3, 0],[3, 1], [3, 2], [3, 3]
        ],
        "red_magnet": null,
        "purple_magnet": [2, 0],
        "iron_pieces": [[1, 2]],
        "allowed_moves": 5
    }
```

## State Space
The state space consists of all possible configurations of the board as pieces are moved. The board transitions from one state to another through valid moves, which involve moving magnets or iron pieces according to their specific movement rules.

## Procedures:

## Main Functions:

### Brute Force Search:
##### Description: Explores all possible moves recursively without any optimization.
##### Function: brute_force_search(board)
##### Helper Function: \_brute_force_recursive(board, all_states, visited)

### BFS (Breadth-First Search):
##### Description: Explores all possible moves level by level using a queue. Finds the shortest path to the solution.
##### Function: bfs_search(board, all_states)

### DFS (Depth-First Search):
##### Description: Explores moves as deeply as possible along each branch before backtracking.
##### Function: dfs_search(board, all_states)

## Additional Functions:
Board Initialization: Initializes the board grid and places pieces according to the configuration.
##### Function: initialize_grid(config)
##### Piece Movement: Handles the movement of pieces on the board and interactions like pushing and pulling.
##### Functions: 
1. move_piece(move)
2. push(board, new_x, new_y)
3. pull(board, new_x, new_y)
## End State
The end state is achieved when all solve cells are occupied by any piece. The game checks for this condition and declares a win if the puzzle is solved within the allowed number of moves.

## How to Run
- Load Levels: Load the level configurations from a JSON file.
```Python
levels = load_levels('levels.json')
```

- Choose Level: Prompt the user to select a level to play.
```Python
selected_level = choose_level(levels)
```

- Start Game: Initialize the game with the selected level and display the board.
```Python
game = LogicMagnetsGame(selected_level)
print(game.board)
```

- Play or Search: Choose to play manually or use search algorithms to solve the puzzle.
```Python
game.play()
```

or
```Python
all_states = brute_force_search(game.board)
bfs_search(game.board, all_states)
dfs_search(game.board, all_states)
```

## Dependencies
- Python 3.x
- json
- collections
- copy

## License
This project is licensed under the MIT License.

