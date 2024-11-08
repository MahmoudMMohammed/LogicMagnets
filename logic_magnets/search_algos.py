from collections import deque


def brute_force_search(board):
    initial_state = board.clone()
    all_states = []
    visited = set()
    _brute_force_recursive(initial_state, all_states, visited)
    return all_states


def _brute_force_recursive(board, all_states, visited):
    board_str = str(board)
    if board_str in visited:
        return

    visited.add(board_str)
    all_states.append(board)

    moves = board.generate_all_possible_moves()

    for move in moves:
        new_board = board.clone()
        new_board.move_piece(move)
        _brute_force_recursive(new_board, all_states, visited)


def bfs_search(board, all_states):
    visited = set()
    queue = deque([(all_states[0], None, None)])  # Each element is a tuple (state, previous_state, move)
    visited.add(str(all_states[0]))
    predecessors = {}  # mapping each state to a tuple (previous_state, move)

    while queue:
        current_state, previous_state, move = queue.popleft()

        if board.is_solved(current_state):
            print("Solution found:")
            solution_path = []
            while current_state is not None:
                solution_path.append((current_state, move))
                current_state, move = predecessors.get(str(current_state), (None, None))
            solution_path.reverse()
            for state, move in solution_path:
                if move:
                    print(f"Move: {move}")
                print(state)
            return solution_path

        moves = current_state.generate_all_possible_moves()
        for move in moves:
            new_state = current_state.clone()
            new_state.move_piece(move)

            if str(new_state) not in visited:
                visited.add(str(new_state))
                queue.append((new_state, current_state, move))
                predecessors[str(new_state)] = (current_state, move)

    print("No solution found after exploring all states.")
    return None


def dfs_search(board, all_states):
    visited = set()
    stack = [(all_states[0], None, None)]
    visited.add(str(all_states[0]))
    predecessors = {}
    while stack:
        current_state, previous_state, move = stack.pop()
        if board.is_solved(current_state):
            print("Solution found:")
            solution_path = []
            while current_state is not None:
                solution_path.append((current_state, move))
                current_state, move = predecessors.get(str(current_state), (None, None))
            solution_path.reverse()
            for state, move in solution_path:
                if move:
                    print(f"Move: {move}")
                print(state)
            return solution_path
        moves = current_state.generate_all_possible_moves()
        for move in moves:
            new_state = current_state.clone()
            new_state.move_piece(move)
            if str(new_state) not in visited:
                visited.add(str(new_state))
                stack.append((new_state, current_state, move))
                predecessors[str(new_state)] = (current_state, move)
    print("No solution found after exploring all states.")
    return None
