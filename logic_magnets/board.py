from logic_magnets.cell import Cell
from logic_magnets.piece import RedMagnet, PurpleMagnet, IronPiece
import copy


class Board:
    def __init__(self, config):
        self.size = config['size']
        self.grid = self.initialize_grid(config)

    def __eq__(self, other):
        if not isinstance(other, Board):
            return NotImplemented
        return self.grid == other.grid

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.grid))

    def clone(self):
        return copy.deepcopy(self)

    def initialize_grid(self, config):
        grid = [[Cell() for _ in range(self.size)] for _ in range(self.size)]

        for x, y in config['solve_cells']:
            if self.is_within_bounds(x, y):
                grid[x][y].is_solve_cell = True
                grid[x][y].is_movable = True
            else:
                print(f"Warning: Solve cell at ({x}, {y}) is out of bounds.")

        for x in range(self.size):
            for y in range(self.size):
                grid[x][y].is_movable = True

        for x, y in config.get('non_movable_cells', []):
            if self.is_within_bounds(x, y):
                grid[x][y].is_movable = False
            else:
                print(f"Warning: Non-movable cell at ({x}, {y}) is out of bounds.")

        red_magnet_pos = config.get('red_magnet')
        if red_magnet_pos:
            x, y = red_magnet_pos
            if self.is_within_bounds(x, y):
                red_magnet = RedMagnet(x, y)
                grid[x][y].piece = red_magnet
            else:
                print(f"Error: Red magnet position at ({x}, {y}) is out of bounds.")

        purple_magnet_pos = config.get('purple_magnet')
        if purple_magnet_pos:
            x, y = purple_magnet_pos
            if self.is_within_bounds(x, y):
                purple_magnet = PurpleMagnet(x, y)
                grid[x][y].piece = purple_magnet
            else:
                print(f"Error: Purple magnet position at ({x}, {y}) is out of bounds.")

        for x, y in config['iron_pieces']:
            if self.is_within_bounds(x, y):
                iron_piece = IronPiece(x, y)
                grid[x][y].piece = iron_piece
            else:
                print(f"Warning: Iron piece at ({x}, {y}) is out of bounds.")

        return grid

    def is_within_bounds(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def move_piece(self, old_x, old_y, new_x, new_y):
        if self.is_within_bounds(new_x, new_y) and self.is_cell_movable(new_x, new_y):
            self.grid[old_x][old_y].piece.move(self, new_x, new_y)
            self.print_board()
            if self.is_solved(self):
                return True
        else:
            print("Cannot move to the specified cell.")

    def is_cell_movable(self, x, y):
        return self.grid[x][y].is_movable

    def print_board(self):
        for row in self.grid:
            print(' '.join([
                '.' if cell.piece is None and cell.is_movable else
                ' ' if not cell.is_movable else
                type(cell.piece).__name__[0]
                for cell in row
            ]))
        print()

    @staticmethod
    def is_solved(board):
        for row in board.grid:
            for cell in row:
                if cell.is_solve_cell and cell.piece is None:
                    return False
        return True
