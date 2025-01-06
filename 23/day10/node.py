class Node:
    def __init__(self, parent=None, position: tuple = None, pipe: str = ''):
        # Where did I come from?
        self.parent = parent
        self.position: tuple = position
        self.pipe = pipe
        assert self.pipe != ''

    def is_visited(self, new_position):
        if self.parent is None:
            return False
        return self.parent.is_visited(new_position) or self.position == new_position

    def __str__(self):
        return f'Pipe: {self.pipe} Position: {self.position}'
