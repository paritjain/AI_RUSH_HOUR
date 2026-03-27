"""

Three sample Rush Hour puzzles (Easy / Medium / Hard).

Each puzzle is a GameState with valid, non-overlapping cars.
The red car 'X' is always horizontal in row 2.
"""
from game_state import Car, GameState
def get_puzzle(level: int = 1) -> GameState:
  if level == 1:
        return _puzzle_easy()
    elif level == 2:
        return _puzzle_medium()
    else:
        return _puzzle_hard()

# Easy Puzzle
def _puzzle_easy() -> GameState:
    return GameState([
        Car('X', 2, 0, 2, 'H'),   # Red car – must reach col 4
        Car('A', 1, 3, 2, 'V'),   # Blocks col 3 in row 2
    ])
# Medium Puzzle
def _puzzle_medium() -> GameState:
    return GameState([
        Car('X', 2, 0, 2, 'H'),   # Red car
        Car('A', 0, 0, 2, 'H'),   # Top-left horizontal
        Car('B', 1, 3, 2, 'V'),   # Blocks col 3 in row 2
        Car('C', 2, 5, 2, 'V'),   # Blocks col 5 (the exit column!)
        Car('D', 4, 2, 2, 'H'),   # Bottom horizontal
    ])
  # Hard Puzzle
def _puzzle_hard() -> GameState:
    return GameState([
        Car('X', 2, 0, 2, 'H'),   # Red car
        Car('A', 0, 2, 3, 'V'),   # Tall blocker in col 2 (rows 0-2)
        Car('B', 0, 4, 2, 'H'),   # Top-right horizontal
        Car('C', 3, 3, 2, 'H'),   # Mid-right horizontal
        Car('D', 4, 1, 2, 'H'),   # Blocks A from sliding down
        Car('E', 5, 3, 2, 'H'),   # Bottom horizontal
    ])



