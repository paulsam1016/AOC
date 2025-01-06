import os
from copy import deepcopy
from math import dist

from colorama import init, Style, Fore

from day23.solve import Node


class Astar:
    def __init__(
            self,
            maze: str,
            start: tuple = None,
            end: tuple = None,
            start_character: str = 'S',
            end_character: str = 'E',
            wall_character: str = '#',
            way_character: str = '.',
            solution_character: str = '+',
            open_character: str = 'o',
            closed_character: str = '*',
            climb_slopes: bool = False
    ):
        self.maze: list[list[str]] = [[*line] for line in maze.splitlines()]
        self.start_character: str = start_character
        self.end_character: str = end_character
        self.wall_character: str = wall_character
        self.way_character: str = way_character
        self.solution_character: str = solution_character
        self.open_character: str = open_character
        self.closed_character: str = closed_character
        self.start: Node = Node(grid=self.maze, parent=None, position=start) if start is not None else None
        self.end: Node = Node(grid=self.maze, parent=None, position=end) if end is not None else None
        self.climb_slopes = climb_slopes

        # Create start and end node if not provided
        if self.start is None and self.end is None:
            self.find_start_and_end()

        assert self.start.position is not None and self.end.position is not None

        # Initialize both open and closed list
        self.open_list: list[Node] = [self.start]
        self.closed_list: list[Node] = []

        # Initialize last checked node
        self.last_checked_node = self.start

        # Initialize solution path
        self.solution_path: list[tuple] = []

        self.slopes = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
        self.adjacent_dir = {
            "S": [(1, 0)],
            "E": [(-1, 0)],
            "^": [(-1, 0)],
            "v": [(1, 0)],
            "<": [(0, -1)],
            ">": [(0, 1)],
            ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
        }

        self.solutions = []

        # Initialize colorama
        init(autoreset=True)

    def find_start_and_end(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == self.start_character:
                    self.start = Node(grid=self.maze, parent=None, position=(i, j))
                if self.maze[i][j] == self.end_character:
                    self.end = Node(grid=self.maze, parent=None, position=(i, j))

    def heuristic(self, a, b):
        d = abs(a[0] - b[0]) + abs(a[1] - b[1])
        return d

    @staticmethod
    def visual_dist(a, b):
        return dist(a, b)

    def print(self, maze=None):
        printable_maze = deepcopy(self.maze) if maze is None else maze
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if printable_maze[i][j] == self.start_character:
                    printable_maze[i][j] = Fore.LIGHTYELLOW_EX + self.start_character + Style.RESET_ALL
                if printable_maze[i][j] == self.end_character:
                    printable_maze[i][j] = Fore.LIGHTYELLOW_EX + self.end_character + Style.RESET_ALL

        print('\n'.join([' '.join(line) for line in printable_maze]))

    def print_solution(self):
        printable_maze = deepcopy(self.maze)
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if (i, j) in self.solution_path:
                    printable_maze[i][j] = Fore.LIGHTBLUE_EX + self.solution_character + Style.RESET_ALL

        self.print(printable_maze)

    def print_solved(self):
        printable_maze = deepcopy(self.maze)
        closed_list = [(item.position[0], item.position[1]) for item in self.closed_list]
        open_list = [(item.position[0], item.position[1]) for item in self.open_list]

        solved = []
        current = self.last_checked_node
        while current is not None:
            solved.append(current.position)
            current = current.parent
        solved = solved[1:-1][::-1]

        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if (i, j) in closed_list and (i, j) != self.start.position and (i, j) != self.end.position:
                    printable_maze[i][j] = Fore.RED + self.closed_character + Style.RESET_ALL
                if (i, j) in open_list and (i, j) != self.start.position and (i, j) != self.end.position:
                    printable_maze[i][j] = Fore.GREEN + self.open_character + Style.RESET_ALL
                if (i, j) in solved:
                    printable_maze[i][j] = Fore.LIGHTBLUE_EX + self.solution_character + Style.RESET_ALL

        self.print(printable_maze)

    def get_path(self, node):
        path = []
        current = node
        while current is not None:
            path.append(current.position)
            current = current.parent
        # print(path)
        return path[1:-1]

    def remove_till_intersection(self, keep, remove):
        keep_path = self.get_path(keep)

        current = remove
        last_node = remove
        while current is not None:
            if current.parent.position in keep_path:
                break
            last_node = current
            current = current.parent

        # print(last_node)
        self.last_checked_node = last_node.parent
        self.closed_list.remove(last_node.parent)
        self.open_list.append(last_node.parent)

        for node in [remove, *self.open_list]:
            path = []
            current = node
            while current is not None:
                path.append(current.position)
                if current.position == last_node.position:
                    break
                current = current.parent
            # print(current.position if current else None, node.position)
            # print(path)
            if current is not None:
                if node in self.open_list:
                    self.open_list.remove(node)
                closed_list_copy = self.closed_list.copy()
                for closed_node in closed_list_copy:
                    if closed_node.position in path and closed_node in self.closed_list:
                        self.closed_list.remove(closed_node)

    def step(self):
        # Loop until you find the end
        if len(self.open_list) > 0:
            # Get the current node
            self.last_checked_node = self.open_list[0]
            current_index = 0
            current_node = self.last_checked_node
            # print([node.l for node in self.closed_list])
            # print(self.last_checked_node.position, self.last_checked_node.f, self.last_checked_node.g, self.last_checked_node.h)
            for index, item in enumerate(self.open_list):
                # print(item.position, item.f, item.g, item.h)
                # Best next option according to the standard heuristic
                if item.l > self.last_checked_node.l:
                    self.last_checked_node = item
                    current_index = index
                    current_node = self.last_checked_node
                # if we have a tie according to the standard heuristic
                if item.l == self.last_checked_node.l:
                    if item.h < self.last_checked_node.h:
                        self.last_checked_node = item
                        current_index = index
                        current_node = self.last_checked_node
                    # if we're using Manhattan distances then also break ties
                    # of the known distance measure by using the visual heuristic.
                    # This ensures that the search concentrates on routes that look
                    # more direct. This makes no difference to the actual path distance
                    # but improves the look for things like games or more closely
                    # approximates the real shortest path if using grid sampled data for
                    # planning natural paths.
                    # if not self.allow_diagonals:
                    #     if item.g == self.last_checked_node.g and item.vh < self.last_checked_node.vh:
                    #         self.last_checked_node = item
                    #         current_index = index
                    #         current_node = self.last_checked_node

            # Found the goal
            if current_node == self.end:
                path = []
                current = self.last_checked_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent

                remove_path = []
                current = self.last_checked_node
                while current is not None:
                    current_position = current.position
                    if self.climb_slopes:
                        adjacent_squares = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    else:
                        adjacent_squares = self.adjacent_dir[self.maze[current_position[0]][current_position[1]]]
                    remove_flag = False
                    for new_position in adjacent_squares:  # Adjacent squares
                        # Get node
                        node_position = (current_position[0] + new_position[0], current_position[1] + new_position[1])
                        if node_position != current_node.position and node_position in [node.position for node in self.open_list]:
                            remove_flag = True
                            break
                    if remove_flag:
                        break

                    remove_path.append(current.position)
                    current = current.parent

                print(current_node.position, remove_path[1:])
                self.last_checked_node = current
                self.open_list.remove(current_node)
                closed_list_copy = self.closed_list.copy()
                for closed_node in closed_list_copy:
                    if closed_node.position in remove_path[1:] and closed_node in self.closed_list:
                        self.closed_list.remove(closed_node)

                path = path[1:-1][::-1]
                self.solutions.append(path)

                # return 1
            else:
                # Pop current off open list, add to closed list
                self.open_list.pop(current_index)
                self.closed_list.append(current_node)
                current_position = current_node.position
                current_character = self.maze[current_position[0]][current_position[1]]

                # Generate neighbors
                neighbors = []
                if self.climb_slopes:
                    adjacent_squares = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                else:
                    adjacent_squares = self.adjacent_dir[current_character]
                for new_position in adjacent_squares:  # Adjacent squares

                    # Get node
                    node_position = (current_position[0] + new_position[0], current_position[1] + new_position[1])

                    # Make sure within range
                    if node_position[0] > (len(self.maze) - 1) or node_position[0] < 0 or node_position[1] > (len(self.maze[len(self.maze) - 1]) - 1) or node_position[1] < 0:
                        continue

                    node_character = self.maze[node_position[0]][node_position[1]]

                    # Make sure walkable terrain
                    if node_character == self.wall_character:
                        continue

                    # Make sure to not climb slope if You cannot climb slopes
                    if not self.climb_slopes and node_character in self.slopes.keys() and self.slopes[node_character] != new_position:
                        continue

                    # Create new node
                    new_node = Node(grid=self.maze, parent=current_node, position=node_position)

                    # Append
                    neighbors.append(new_node)

                # Loop through neighbors
                for neighbor in neighbors:
                    # if current_position == (11, 20):
                    # print([node.position for node in self.closed_list])
                    # print(current_position, neighbor.position)
                    # print(neighbor in self.closed_list, neighbor.position == current_node.parent.position)
                    # print(neighbor in self.open_list, current_node.l <= neighbor.l)

                    # neighbor is on the closed list
                    if neighbor in self.closed_list:
                        if neighbor.position == current_node.parent.position:
                            continue
                        elif current_node.l > self.closed_list[self.closed_list.index(neighbor)].l:
                            # print('-------------------------')
                            # print(current_position, current_character)
                            # print(neighbor.position, self.maze[neighbor.position[0]][neighbor.position[1]])
                            # print(current_node.l, self.closed_list[self.closed_list.index(neighbor)].l)
                            # print([node.position for node in self.open_list])
                            for node in self.open_list:
                                path = []
                                current = node
                                while current is not None:
                                    path.append(current.position)
                                    if current.position == neighbor.position:
                                        break
                                    current = current.parent
                                if current is not None:
                                    self.open_list.remove(node)
                                    for closed_node in self.closed_list:
                                        if closed_node.position in path:
                                            self.closed_list.remove(closed_node)
                        else:
                            continue

                    # print(temp_h)
                    # print(temp_g)
                    # print(neighbor.g)

                    # Is this a better path than before(open_list)
                    if neighbor in self.open_list:
                        print(current_node.position, neighbor.position)
                        print(current_node.l, self.open_list[self.open_list.index(neighbor)].l)
                        # print([node.position for node in self.open_list])

                        if current_node.l > self.open_list[self.open_list.index(neighbor)].l:
                            removed_node = self.open_list.pop(self.open_list.index(neighbor))
                            self.remove_till_intersection(keep=current_node, remove=removed_node)
                            # print([node.position for node in self.open_list])
                        else:
                            print('remove current_node')
                            self.remove_till_intersection(keep=self.open_list[self.open_list.index(neighbor)], remove=current_node)
                            break

                    neighbor.h = self.heuristic(neighbor.position, self.end.position)
                    neighbor.l = current_node.l + 1

                    # Add the neighbor to the open list
                    if neighbor not in self.open_list:
                        self.open_list.append(neighbor)
                return 0
        else:
            return -1

    def solve(self):
        # Loop until you find the end
        while len(self.open_list) > 0:
            result = self.step()
            # print(result)
            # print([node.position for node in self.open_list])
            if result == 1:
                path = []
                current = self.last_checked_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                path = path[1:-1][::-1]
                self.solution_path = path
                return 1
            if result == -1:
                return -1
        if self.solutions:
            self.solution_path = self.solutions[0]

    def solve_step_by_step(self):
        # Loop until you find the end
        while len(self.open_list) > 0:
            # os.system('cls' if os.name == 'nt' else 'clear')
            result = self.step()
            if result == 1:
                path = []
                current = self.last_checked_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                path = path[1:-1][::-1]
                self.solution_path = path
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.LIGHTRED_EX + 'Goal Reached!')
                break
            if result == -1:
                print(Fore.LIGHTGREEN_EX + 'No Solution!')
                break
            self.print_solved()
            # sleep(0.3)
        self.print_solved()
        if self.solutions:
            self.solution_path = self.solutions[0]
