class Cell:
    def __init__(self, is_movable=False, is_solve_cell=False, piece=None, cost=1):
        self.is_movable = is_movable
        self.is_solve_cell = is_solve_cell
        self.piece = piece
        self.cost = cost
