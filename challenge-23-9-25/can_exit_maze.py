class Node:
    """
    __summary__:
        A special datatype containing information a particular cell in a grid

    Attributes:
        position: list[int] ==> position of the node on the grid
        parent: Node ==> The parent node. The default value of None applies to the starting position on the grid
    """
    def __init__(self, position: list[int], parent=None):
        self.position = position
        self.parent = parent


class Visited:
    """_summary_:
        A datatype for holding the list of visited positions on the grid

    Attributes:
        visited: list[list] ==> A list of visited positions on the grid.

    methods:
        add(self, position: list[int]) ==> A void function for appending new positions to the list
        contains(self, position: list[int]) -> bool ==> to check if a position is already present in the list
    """

    def __init__(self):
        self.visited: list[list] = []

    def add(self, position: list[int]):
        self.visited.append(position)

    def contains(self, position: list[int]) -> bool:
        return position in self.visited


class DFS_frontier:
    """
    _summary_:
        A class to represent the frontier (or open set) of nodes to be explored in the search algorithm.
        This implementation uses a stack (LIFO) approach. Thus it is a Depth-First Search (DFS).

    Attributes:
        frontier (list) ==> A list to store the nodes in the frontier.

    methods:
        add(self, node: Node) ==> A void function for appending new nodes to the frontier
        remove(self) -> Node ==> A function to pop out a node from the frontier. Raises an exception if the frontier is empty
        empty(self) -> bool ==> A function for checking if the frontier is empty
    """

    def __init__(self):
        self.frontier = []

    def add(self, node: Node):
        self.frontier.append(node)

    def remove(self) -> Node:
        if self.empty():
            raise Exception("Frontier is empty")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

    def empty(self) -> bool:
        return len(self.frontier) == 0


def up(current_pos: list, grid: list[list])-> list:
    """ checks if the cell above current cell is a path or an obstacle """

    row = current_pos[0] - 1
    col = current_pos[1]
    if (row >= 0) and (grid[row][col] == 0):
        return [row, col]
    return None

def down(current_pos: list, grid: list[list])-> list:
    """ checks if the cell below current cell is a path or an obstacle """

    row = current_pos[0] + 1
    col = current_pos[1]
    if (row < len(grid)) and (grid[row][col] == 0):
        return [row, col]
    return None

def right(current_pos: list, grid: list[list])-> list:
    """ checks if the cell to the right of the current cell is a path or an obstacle """

    row = current_pos[0]
    col = current_pos[1] + 1
    if (col < len(grid[0])) and (grid[row][col] == 0):
        return [row, col]
    return None

def left(current_pos: list, grid: list[list])-> list:
    """ checks if the cell to the left of the current cell is a path or an obstacle """

    row = current_pos[0]
    col = current_pos[1] - 1
    if (col >= 0) and (grid[row][col] == 0):
        return [row, col]
    return None

def next_paths(node: Node, grid: list[list]) -> list[Node]:
    nodes = []
    current_position = node.position
    func_calls = [up(current_position, grid), left(current_position, grid), down(current_position, grid), right(current_position, grid)]

    for position in func_calls:
        if position and (position not in nodes):
            next_path = Node(position=position, parent=node)
            nodes.append(next_path)
    if nodes:
        return nodes
    return None


def canExit(grid: list[list]) -> bool:
    frontier = DFS_frontier()
    visited = Visited()
    start = Node(position=[0, 0])

    goal = [len(grid) - 1, len(grid[0]) - 1]
    frontier.add(start)
    while not frontier.empty():
        current_cell = frontier.remove()
        if current_cell.position == goal:
            return True
        next = next_paths(current_cell, grid)
        visited.add(current_cell.position)
        if next:
            for point in next:
                if not visited.contains(point.position):
                    frontier.add(point)
    return False
