def check_up(letter_pos: list, grid: list[list])-> str:
    """ return the element in the cell above the current cell """

    if (letter_pos[0] - 1) >= 0:
        return grid[letter_pos[0] - 1][letter_pos[1]]
    return None

def check_down(letter_pos: list, grid: list[list])-> str:
    """ return the element in the cell below the current cell """

    if (letter_pos[0] + 1) < len(grid):
        return grid[letter_pos[0] + 1][letter_pos[1]]
    return None

def check_right(letter_pos: list, grid: list[list])-> str:
    """ return the element in the cell to the right of the current cell """

    if (letter_pos[1] + 1) < len(grid[0]):
        return grid[letter_pos[0]][letter_pos[1] + 1]
    return None

def check_left(letter_pos: list, grid: list[list])-> str:
    """ return the element in the cell to the left of the current cell """
    if (letter_pos[1] - 1) >= 0:
        return grid[letter_pos[0]][letter_pos[1] - 1]
    return None


def look_around(row_pos: int, col_pos: int, objective: str, grid: list[list])-> list:
    """ Search neighbouring the cells for the location of the objective """

    letter_pos = [row_pos, col_pos]
    grid = grid

    func_calls = [check_up(letter_pos, grid), check_right(letter_pos, grid), check_down(letter_pos, grid), check_left(letter_pos, grid)]

    up = [row_pos-1, col_pos]
    right = [row_pos, col_pos+1]
    down = [row_pos+1, col_pos]
    left = [row_pos, col_pos-1]

    positions = [up, right, down, left]

    captured = []

    if objective == grid[row_pos][col_pos]:
        captured.append([row_pos, col_pos])
    else:
        for i in range(len(func_calls)):
            if objective == func_calls[i]:
                captured.append(positions[i])
    if captured:
        return captured
    return None


def trace_word_path(word: str, grid: list[list])-> list[list]:
    """_summary_:
            A function for searching if a word can be traced out in a grid of letters along horizontal or vertical directions

    Assumptions:
        The grid is assumped to be a list of lists of equal sizes.
        All letters are uppercase

    Args:
        word (str): The word to be searched in the grid of letters
        grid (list[list]): The grid of letters

    Returns:
        list[list]: coordinates of the letters of the searched word in the grid
    """

    output = []
    letters = list(word)
    first_pos = None
    alternate_start = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            first_pos = look_around(row, col, letters[0], grid)
            if first_pos:
                for pos in first_pos:
                    if pos not in alternate_start:
                        alternate_start.append(pos)

    if alternate_start:
        for start in alternate_start:
            if look_around(start[0], start[1], letters[1], grid):
                output.append(start)
                current_pos = start
            else:
                continue

            for i in range(1, len(letters)):
                new_pos = look_around(current_pos[0], current_pos[1], letters[i], grid)
                if new_pos:
                    if len(new_pos) == 1 and (new_pos[0] not in output):
                        output.append(new_pos[0])
                        current_pos = new_pos[0]
                    elif len(new_pos) > 1:
                        mid_alternatives = []
                        for index in new_pos:
                            mid_alternatives.append(index)
                        for alt in mid_alternatives:
                            if i < (len(letters) - 1):
                                check_alt = look_around(alt[0], alt[1], letters[i + 1], grid)
                            if check_alt and (alt not in output):
                                output.append(alt)
                                current_pos = alt
                else:
                    output = []
                    break

            if len(output) == len(letters):
                return output
            output = []
    return "Not present"
