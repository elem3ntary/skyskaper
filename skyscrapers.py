'''
Skyskaper game
'''


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    with open(path, 'r') as file:
        return file.readlines()


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    >>> left_to_right_check("423145*", 4)
    True
    """
    input_line = input_line[1:6]
    previous = 0
    visible = 0
    for height in input_line:
        height = int(height)
        if height > previous:
            visible += 1
            previous = height
    return visible == pivot


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', \
'*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', \
'*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        if '?' in set(row):
            return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', \
'*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:6]
    for row in board:
        row = row[1:6]
        if len(set(row)) != len(row):
            return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:6]
    for row in board:
        if row.count('*') == 2:
            continue
        if '*' != row[0]:
            if not left_to_right_check(row, int(row[0])):
                return False
        if '*' != row[6]:
            row = ''.join(reversed(list(row)))
            if not left_to_right_check(row, int(row[0])):
                return False
    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) \
and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.


    >>> check_columns(['***21**', '412453*', '423145*', '*542315', '*35214*', '*41532*', '*2*1***'])
    False
    """
    columns = []
    for i in range(7):
        column = ''
        for row in board:
            column += row[i]
        columns.append(column)
    return check_horizontal_visibility(columns)


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)
    if not check_not_finished_board(board):
        return False
    if not check_uniqueness_in_rows(board):
        return False
    if not check_horizontal_visibility(board):
        return False
    if not check_columns(board):
        return False
    return True


if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    doctest.run_docstring_examples(check_columns, globals())
    # print(check_skyscrapers("check.txt"))
