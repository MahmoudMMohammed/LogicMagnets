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

        def are_iron_pieces_adjacent(pos1, pos2):
            return (pos1[0] == pos2[0] and abs(pos1[1] - pos2[1]) == 1) or \
                (pos1[1] == pos2[1] and abs(pos1[0] - pos2[0]) == 1)

        pushed_positions = set()

        for i in range(len(iron_positions)):
            iron_x, iron_y = iron_positions[i]

            if (iron_x, iron_y) in pushed_positions:
                continue

            if i < len(iron_positions) - 1:
                next_iron_x, next_iron_y = iron_positions[i + 1]

                if are_iron_pieces_adjacent((iron_x, iron_y), (next_iron_x, next_iron_y)):
                    if iron_y == next_iron_y:
                        print("same column")
                        direction = -1 if iron_x < new_x else 1
                        target_y = iron_y
                        first_target_x = next_iron_x + direction
                        second_target_x = iron_x + direction

                        if board.is_within_bounds(iron_x, target_y) and \
                                ((board.grid[first_target_x][target_y].piece is None) or (
                                        board.grid[second_target_x][target_y].piece is None)) and \
                                ((board.is_cell_movable(first_target_x, target_y)) or (
                                        board.is_cell_movable(second_target_x, target_y))):
                            print(f"Pushing Iron piece at ({next_iron_x}, {iron_y}) to ({first_target_x}, {target_y})")
                            board.grid[first_target_x][target_y].piece = board.grid[next_iron_x][iron_y].piece
                            board.grid[next_iron_x][iron_y].piece = None

                            print(f"Pushing Iron piece at ({iron_x}, {iron_y}) to ({second_target_x}, {target_y})")
                            board.grid[next_iron_x][iron_y].piece = board.grid[iron_x][iron_y].piece
                            board.grid[iron_x][iron_y].piece = None

                            pushed_positions.add((iron_x, iron_y))
                            pushed_positions.add((next_iron_x, next_iron_y))
                            break

                    if iron_x == next_iron_x:
                        print("same row")
                        direction = -1 if iron_y < new_y else 1
                        target_x = iron_x
                        first_target_y = next_iron_y + direction
                        second_target_y = iron_y + direction

                        if board.is_within_bounds(target_x, iron_y) and \
                                ((board.grid[target_x][first_target_y].piece is None) or (
                                        board.grid[target_x][second_target_y].piece is None)) and \
                                ((board.is_cell_movable(target_x, first_target_y)) or (
                                        board.is_cell_movable(target_x, second_target_y))):
                            print(f"Pushing Iron piece at ({iron_x}, {next_iron_y}) to ({target_x}, {first_target_y})")
                            board.grid[target_x][first_target_y].piece = board.grid[iron_x][iron_y].piece
                            board.grid[iron_x][next_iron_y].piece = None

                            print(f"Pushing Iron piece at ({iron_x}, {iron_y}) to ({target_x}, {second_target_y})")
                            board.grid[target_x][second_target_y].piece = board.grid[iron_x][iron_y].piece
                            board.grid[iron_x][iron_y].piece = None

                            pushed_positions.add((iron_x, iron_y))
                            pushed_positions.add((next_iron_x, next_iron_y))
                            break

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
