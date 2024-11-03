from logic_magnets.board import Board


class LogicMagnetsGame:
    def __init__(self, level_config):
        self.level_config = level_config
        self.board = Board(level_config)
        self.allowed_moves = level_config['allowed_moves']
        self.current_moves = 0
        self.previous_boards = []

    def play(self):
        current_board = self.board
        current_board.print_board()
        self.previous_boards.append(current_board)
        while self.current_moves < self.allowed_moves:
            try:
                x = int(input("Enter x coordinate of the piece to move: "))
                y = int(input("Enter y coordinate of the piece to move: "))
                new_x = int(input("Enter new x coordinate: "))
                new_y = int(input("Enter new y coordinate: "))
                piece = current_board.grid[x][y].piece
                if piece:
                    solved = self.board.move_piece(x, y, new_x, new_y)
                    if solved:
                        print("Congratulations! You've solved the puzzle!")
                        break
                    new_board = current_board.clone()
                    current_board = new_board
                    self.previous_boards.append(new_board)
                    self.current_moves += 1
                else:
                    print("No piece at this position.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid coordinates.")

        if self.current_moves >= self.allowed_moves:
            print("Out of moves. Game over.")
