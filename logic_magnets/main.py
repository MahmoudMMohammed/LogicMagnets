from logic_magnets.game import LogicMagnetsGame
import json


def load_levels(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def choose_level(levels):
    print("Available Levels:")
    for i, level in enumerate(levels):
        print(f"Level {i + 1}: {level['size']}x{level['size']} Grid")

    level_choice = int(input("Select the level you want to play (1-{}): ".format(len(levels)))) - 1

    if level_choice < 0 or level_choice >= len(levels):
        print("Invalid choice. Please select a valid level.")
        return choose_level(levels)

    return levels[level_choice]


levels = load_levels('levels.json')

if __name__ == '__main__':
    selected_level = choose_level(levels)

    game = LogicMagnetsGame(selected_level)
    print(f"Solve cells are: {selected_level['solve_cells']}")
    game.play()
