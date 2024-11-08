class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, board, new_x, new_y):
        pass

    def update_position(self, board, new_x, new_y):
        if board.grid[new_x][new_y].piece is None:
            board.grid[self.x][self.y].piece = None
            self.x, self.y = new_x, new_y
            board.grid[new_x][new_y].piece = self
            return True
        else:

            return False


class PurpleMagnet(Piece):
    def move(self, board, new_x, new_y):
        if board.is_within_bounds(new_x, new_y):
            if self.update_position(board, new_x, new_y):
                self.push(board, new_x, new_y)
            else:
                print("Piece is already occupied")

    @staticmethod
    def push(board, new_x, new_y):
        vertical_iron_positions = []
        horizontal_iron_positions = []

        for j in range(board.size):
            if isinstance(board.grid[new_x][j].piece, (IronPiece, RedMagnet)):
                horizontal_iron_positions.append((new_x, j))

        for i in range(board.size):
            if isinstance(board.grid[i][new_y].piece, (IronPiece, RedMagnet)):
                vertical_iron_positions.append((i, new_y))

        vertical_iron_positions.sort(key=lambda pos: (abs(pos[0] - new_x) + abs(pos[1] - new_y)))
        horizontal_iron_positions.sort(key=lambda pos: (abs(pos[0] - new_x) + abs(pos[1] - new_y)))

        iron_positions = vertical_iron_positions + horizontal_iron_positions

        pushed_positions = set()

        for i in range(len(iron_positions)):
            iron_x, iron_y = iron_positions[i]

            if (iron_x, iron_y) in pushed_positions:
                continue

            if iron_y < new_y:
                target_y = iron_y - 1
                if board.is_within_bounds(iron_x, target_y) and \
                        board.grid[iron_x][target_y].piece is None and \
                        board.is_cell_movable(iron_x, target_y):
                    print(f"Pushing Iron piece at ({iron_x}, {iron_y}) to ({iron_x}, {target_y})")
                    board.grid[iron_x][target_y].piece = board.grid[iron_x][iron_y].piece
                    board.grid[iron_x][iron_y].piece = None
                    pushed_positions.add((iron_x, iron_y))

            elif iron_y > new_y:
                target_y = iron_y + 1
                if board.is_within_bounds(iron_x, target_y) and \
                        board.grid[iron_x][target_y].piece is None and \
                        board.is_cell_movable(iron_x, target_y):
                    print(f"Pushing Iron piece at ({iron_x}, {iron_y}) to ({iron_x}, {target_y})")
                    board.grid[iron_x][target_y].piece = board.grid[iron_x][iron_y].piece
                    board.grid[iron_x][iron_y].piece = None
                    pushed_positions.add((iron_x, iron_y))

            elif iron_x < new_x:
                target_x = iron_x - 1
                if board.is_within_bounds(target_x, iron_y) and \
                        board.grid[target_x][iron_y].piece is None and \
                        board.is_cell_movable(target_x, iron_y):
                    print(f"Pushing Iron piece at ({iron_x}, {iron_y}) to ({target_x}, {iron_y})")
                    board.grid[target_x][iron_y].piece = board.grid[iron_x][iron_y].piece
                    board.grid[iron_x][iron_y].piece = None
                    pushed_positions.add((iron_x, iron_y))

            elif iron_x > new_x:
                target_x = iron_x + 1
                if board.is_within_bounds(target_x, iron_y) and \
                        board.grid[target_x][iron_y].piece is None and \
                        board.is_cell_movable(target_x, iron_y):
                    print(f"Pushing Iron piece at ({iron_x}, {iron_y}) to ({target_x}, {iron_y})")
                    board.grid[target_x][iron_y].piece = board.grid[iron_x][iron_y].piece
                    board.grid[iron_x][iron_y].piece = None
                    pushed_positions.add((iron_x, iron_y))


class RedMagnet(Piece):
    def move(self, board, new_x, new_y):
        if board.is_within_bounds(new_x, new_y):
            if self.update_position(board, new_x, new_y):
                self.pull(board, new_x, new_y)
            else:
                print("Piece is already occupied")

    @staticmethod
    def pull(board, new_x, new_y):
        vertical_iron_positions = []
        horizontal_iron_positions = []

        for j in range(board.size):
            if isinstance(board.grid[new_x][j].piece, (IronPiece, RedMagnet)):
                horizontal_iron_positions.append((new_x, j))

        for i in range(board.size):
            if isinstance(board.grid[i][new_y].piece, (IronPiece, RedMagnet)):
                vertical_iron_positions.append((i, new_y))

        vertical_iron_positions.sort(key=lambda pos: (abs(pos[0] - new_x) + abs(pos[1] - new_y)))
        horizontal_iron_positions.sort(key=lambda pos: (abs(pos[0] - new_x) + abs(pos[1] - new_y)))

        iron_positions = vertical_iron_positions + horizontal_iron_positions

        for iron_x, iron_y in iron_positions:
            if iron_y < new_y:
                target_y = iron_y + 1
                if board.is_within_bounds(iron_x, target_y) and \
                        board.grid[iron_x][target_y].piece is None and \
                        board.is_cell_movable(iron_x, target_y):
                    print(f"Pulling Iron piece at ({iron_x}, {iron_y}) to ({iron_x}, {target_y})")
                    board.grid[iron_x][target_y].piece = board.grid[iron_x][iron_y].piece
                    board.grid[iron_x][iron_y].piece = None

            elif iron_y > new_y:
                target_y = iron_y - 1
                if board.is_within_bounds(iron_x, target_y) and \
                        board.grid[iron_x][target_y].piece is None and \
                        board.is_cell_movable(iron_x, target_y):
                    print(f"Pulling Iron piece at ({iron_x}, {iron_y}) to ({iron_x}, {target_y})")
                    board.grid[iron_x][target_y].piece = board.grid[iron_x][iron_y].piece
                    board.grid[iron_x][iron_y].piece = None

            elif iron_x < new_x:
                target_x = iron_x + 1
                if board.is_within_bounds(target_x, iron_y) and \
                        board.grid[target_x][iron_y].piece is None and \
                        board.is_cell_movable(target_x, iron_y):
                    print(f"Pulling Iron piece at ({iron_x}, {iron_y}) to ({target_x}, {iron_y})")
                    board.grid[target_x][iron_y].piece = board.grid[iron_x][iron_y].piece
                    board.grid[iron_x][iron_y].piece = None

            elif iron_x > new_x:
                target_x = iron_x - 1
                if board.is_within_bounds(target_x, iron_y) and \
                        board.grid[target_x][iron_y].piece is None and \
                        board.is_cell_movable(target_x, iron_y):
                    print(f"Pulling Iron piece at ({iron_x}, {iron_y}) to ({target_x}, {iron_y})")
                    board.grid[target_x][iron_y].piece = board.grid[iron_x][iron_y].piece
                    board.grid[iron_x][iron_y].piece = None


class IronPiece(Piece):
    def move(self, board, new_x, new_y):
        if board.is_within_bounds(new_x, new_y):
            self.update_position(board, new_x, new_y)
