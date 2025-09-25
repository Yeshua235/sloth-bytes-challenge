
def check_up(letter_pos: list, grid: list[list])-> str:
    if (letter_pos[0] - 1) >= 0:
        return grid[letter_pos[0] - 1][letter_pos[1]]
    else:
        return None

def check_down(letter_pos: list, grid: list[list])-> str:
    if (letter_pos[0] + 1) < len(grid):
        return grid[letter_pos[0] + 1][letter_pos[1]]
    else:
        return None

def check_right(letter_pos: list, grid: list[list])-> str:
    if (letter_pos[1] + 1) < len(grid[0]):
        return grid[letter_pos[0]][letter_pos[1] + 1]
    else:
        return None

def check_left(letter_pos: list, grid: list[list])-> str:
    if (letter_pos[1] - 1) >= 0:
        return grid[letter_pos[0]][letter_pos[1] - 1]
    else:
        return None


def look_around(row_pos: int, col_pos: int, objective: str, grid: list[list])-> list:
    """ Search neighbouring cells """
    letter_pos = [row_pos, col_pos]
    grid = grid

    func_calls = [check_up(letter_pos, grid), check_left(letter_pos, grid), check_down(letter_pos, grid), check_right(letter_pos, grid)]

    up = [row_pos-1, col_pos]
    right = [row_pos, col_pos+1]
    down = [row_pos+1, col_pos]
    left = [row_pos, col_pos-1]

    positions = [up, left, down, right]

    if objective == grid[row_pos][col_pos]:
        return [row_pos, col_pos]
    else:
        for i in range(len(func_calls)):
            if objective == func_calls[i]:
                return positions[i]
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

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            first_pos = look_around(row, col, letters[0], grid)
            if first_pos:
                output.append(first_pos)
                break
        if first_pos:
            break

    if output:
        current_pos = output[0]
        for i in range(1, len(letters)):
            new_pos = look_around(current_pos[0], current_pos[1], letters[i], grid)
            if new_pos:
                output.append(new_pos)
                current_pos = new_pos
            else:
                print(output)
                return "Not present"

    return output
