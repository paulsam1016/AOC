class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, grid: list[list[str]], parent=None, position: tuple = None):
        self.grid: list[list[str]] = grid

        # Where did I come from?
        self.parent = parent
        self.position: tuple = position

        # A* Pathfinding variables
        self.h = 0
        self.l = 0
        self.vh = 0  # visual heuristic for prioritising path options

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return str(self.position)
