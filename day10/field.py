import os
from math import ceil
from time import sleep

from colorama import Fore, Style, init

from day10.node import Node


class Field:
    def __init__(
            self,
            maze: list[list[str]],
    ):
        self.maze: list[list[str]] = maze
        start_location = ()
        self.possible_pipe_locations = {
            "S": [(-1, 0), (0, 1), (1, 0), (0, -1)],
            ".": [],
            "|": [(1, 0), (-1, 0)],
            "-": [(0, 1), (0, -1)],
            "L": [(0, 1), (-1, 0)],
            "J": [(0, -1), (-1, 0)],
            "7": [(0, -1), (1, 0)],
            "F": [(0, 1), (1, 0)],
        }
        self.possible_pipes = {
            (-1, 0): ['|', '7', 'F'],
            (0, 1): ['-', 'J', '7'],
            (1, 0): ['|', 'L', 'J'],
            (0, -1): ['-', 'L', 'F'],
        }
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 'S':
                    start_location = (i, j)
                    break

        self.start = Node(position=start_location, pipe='S')
        print(start_location)
        self.pipe_path: list[Node] = []
        self.open_list: list[Node] = []
        self.closed_list: list[Node] = []
        self.open_list.append(self.start)
        self.last_checked_node = self.start

        # Initialize colorama
        init(autoreset=True, )

    def get_path(self, node):
        current_node = node
        path = []
        while current_node.parent is not None:
            path.append(current_node)
            current_node = current_node.parent
        path.append(self.start)
        return path

    def print(self, maze=None):
        printable_maze = self.maze if maze is None else maze
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if printable_maze[i][j] == 'S':
                    printable_maze[i][j] = Fore.LIGHTYELLOW_EX + printable_maze[i][j] + Style.RESET_ALL

        print('\n'.join([''.join(line) for line in printable_maze]))

    def print_solution(self, maze=None):
        printable_maze = self.maze if maze is None else maze
        solution_path = [node.position for node in self.get_path(self.last_checked_node)]
        middle = solution_path[ceil((len(solution_path)) / 2)]
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if (i, j) in solution_path and (i, j) != self.start.position and (i, j) != middle:
                    printable_maze[i][j] = Fore.LIGHTBLUE_EX + printable_maze[i][j] + Style.RESET_ALL
                if middle == (i, j):
                    printable_maze[i][j] = Fore.LIGHTMAGENTA_EX + printable_maze[i][j] + Style.RESET_ALL

        self.print(printable_maze)

    def print_enclosed_solution(self):
        printable_maze = self.maze
        solution_path = [node.position for node in self.get_path(self.last_checked_node)]
        for x in range(len(self.maze)):
            for y in range(len(self.maze[0])):
                if (x, y) in solution_path:
                    continue
                # Point a ray in one direction
                # Main idea is to count crossing with vertical bars
                # But we need to consider corners that cancel each other out:
                #    - LJ for the top horizontal parity (line will stay at the top)
                #    - F7 for the bottom horizontal parity (line will stay at the bottom)
                par_bottom = par_top = 0
                for ny in range(y + 1):
                    if (x, ny) in solution_path and self.maze[x][ny] in "|JL":
                        par_top ^= 1
                    if (x, ny) in solution_path and self.maze[x][ny] in "|F7":
                        par_bottom ^= 1
                if par_bottom and par_top:
                    printable_maze[x][y] = Fore.LIGHTWHITE_EX + printable_maze[x][y] + Style.RESET_ALL
                else:
                    printable_maze[x][y] = Fore.BLACK + printable_maze[x][y] + Style.RESET_ALL
        self.print(printable_maze)
        self.print_solution(printable_maze)

    def print_solved(self):
        printable_maze = self.maze
        closed_list = [(item.position[0], item.position[1]) for item in self.closed_list]
        open_list = [(item.position[0], item.position[1]) for item in self.open_list]

        current = self.last_checked_node
        solved = [node.position for node in self.get_path(current)]

        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if (i, j) in closed_list and (i, j) != self.start.position and (i, j) != self.start.position:
                    printable_maze[i][j] = Fore.RED + printable_maze[i][j] + Style.RESET_ALL
                if (i, j) in open_list and (i, j) != self.start.position and (i, j) != self.start.position:
                    printable_maze[i][j] = Fore.GREEN + printable_maze[i][j] + Style.RESET_ALL
                if (i, j) in solved:
                    printable_maze[i][j] = Fore.LIGHTBLUE_EX + printable_maze[i][j] + Style.RESET_ALL

        self.print(printable_maze)

    def step(self):
        if len(self.open_list) > 0:
            self.last_checked_node = self.open_list[0]
            current_index = 0

            for i in range(len(self.open_list)):
                for j in range(i + 1, len(self.open_list) - i):
                    if self.open_list[i].pipe == self.open_list[j].pipe and self.open_list[i].position == self.open_list[j].position:
                        path = self.get_path(self.open_list[i])[::-1]

                        for index, node in enumerate(self.get_path(self.open_list[j])[1:-1]):
                            path.append(Node(parent=path[-1], position=node.position, pipe=node.pipe))

                        self.last_checked_node = path[-1]
                        # print('Met at middle')
                        return 1

            # for index, item in enumerate(self.open_list):
            #     # Best next option according to the standard heuristic
            #     if item.path_length() > self.last_checked_node.path_length():
            #         self.last_checked_node = item
            #         current_index = index

            # Pop current off open list, add to closed list
            self.open_list.pop(current_index)
            self.closed_list.append(self.last_checked_node)
            # current_path_length = self.last_checked_node.path_length()

            # print(f'current_node: {str(self.last_checked_node)}')

            # Generate neighbors
            neighbors = []
            for possible_location in self.possible_pipe_locations[self.last_checked_node.pipe]:

                # Get new location
                new_location = (self.last_checked_node.position[0] + possible_location[0], self.last_checked_node.position[1] + possible_location[1])

                # print(f'{new_location=}')

                # Make sure within range
                if new_location[0] > (len(self.maze) - 1) or new_location[0] < 0 or new_location[1] > (len(self.maze[0]) - 1) or new_location[1] < 0:
                    continue

                # Make sure new_location is not last_node.parent.position to stop infinite looping
                if self.last_checked_node.parent and self.last_checked_node.parent.position == new_location:
                    # print(f'{new_location} failed already visited')
                    continue

                # Get pipe at location
                new_pipe = self.maze[new_location[0]][new_location[1]]
                # print(f'{new_pipe=}')

                # check if pipe is a valid pipe for location
                if new_pipe not in self.possible_pipes[possible_location]:
                    # print(f'{new_pipe} failed not a possible_pipe')
                    continue

                # Create new node
                new_node = Node(parent=self.last_checked_node, position=new_location, pipe=new_pipe)

                # check if new_node is in the closed list
                if new_node in self.closed_list:
                    # print(f'{str(new_node)} failed in closed_list')
                    continue

                # Is this a better path than before(open_list)
                # if neighbor in open_list and temp_g >= neighbor.:
                #     print(temp_g >= neighbor.g)
                #     continue

                # print(f'new_node: {str(new_node)}')

                # Add the neighbor to the open list
                if new_node not in self.open_list:
                    self.open_list.append(new_node)

                # Append
                neighbors.append(new_node)

            # print([str(neighbor) for neighbor in neighbors])
            # print([neighbor not in self.open_list for neighbor in neighbors])
            # print([neighbor.pipe for neighbor in neighbors])

            # Loop through neighbors
            if all(neighbor not in self.open_list for neighbor in neighbors) and any(neighbor.pipe == 'S' for neighbor in neighbors):
                # print('---------Only S remains------------')
                return 1

            return 0
        else:
            return -1

    def solve(self):
        # Loop until you find the end
        while len(self.open_list) > 0:
            result = self.step()
            if result == 1:
                return 1
            if result == -1:
                return -1
            # print([str(node) for node in self.open_list])
            # print('============================')

    def solve_step_by_step(self):
        # Loop until you find the end
        while len(self.open_list) > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            result = self.step()
            # print(result)
            # print(len(self.open_list))
            if result == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.LIGHTRED_EX + 'Goal Reached!')
                return 1
            if result == -1:
                print(Fore.LIGHTGREEN_EX + 'No Solution!')
                return -1
            # print([str(node) for node in self.open_list])
            self.print_solved()
            sleep(0.5)
        self.print_solved()
