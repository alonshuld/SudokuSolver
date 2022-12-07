CHAR_SPLIT = ' '


def check_puzzle_file(file_name):
    """
    This function checks if a file is valid to be used as a puzzle
    :param file_name: string that contains the file name
    :return: bool answer
    """
    with open(file_name, 'r') as file:
        if len(file.readlines()) != 9:
            return False
        file.seek(0)
        for line in file.readlines():
            line = line.strip()
            if len(line) != 17:
                return False
            for i in range(len(line)):
                if i % 2 == 0:
                    if line[i] < '0' or line[i] > '9':
                        return False
                else:
                    if line[i] != CHAR_SPLIT:
                        return False
    return True


def load_puzzle(file_name):
    """
    This function loads a puzzle from txt file
    :param file_name: a string that contains the file name
    :return: returns a list
    """
    if not check_puzzle_file(file_name):
        print("The file is corrupted")
        exit()
    board = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            board.append(list(map(int, line.strip().split(CHAR_SPLIT))))
    return board


def find_empty_cell(board):
    """
    This function returns a position of an empty cell
    :param board: a 2D array that contains the game
    :return: tuple of position in the 2D array
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # empty cell
                return i, j


def check_num_valid(board, num, pos):
    """
    This function checks if {num} is valid in {pos}
    :param board: a 2D list that contains the board
    :param num: char that represent the number we want to try to put in the cell
    :param pos: tuple that contains the position of the cell this function checks
    :return: bool answer to if the number is valid or not
    """
    # Check row
    for i in range(9):
        if board[pos[0]][i] == num and i != pos[1]:
            return False

    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and i != pos[0]:
            return False

    # Check block
    first_cell_in_block = ((pos[0] // 3) * 3, (pos[1] // 3) * 3)
    for i in range(first_cell_in_block[0], first_cell_in_block[0] + 3):
        for j in range(first_cell_in_block[1], first_cell_in_block[1] + 3):
            if board[i][j] == num and i != pos[0] and j != pos[1]:
                return False

    return True


def print_board(board):
    """
    This function prints the board
    :param board: a 2D array of the board
    :return: None
    """
    for i in range(9):
        if i % 3 == 0:
            print("*-------*-------*-------*")
        for j in range(9):
            if j % 3 == 0:
                print("| ", end="")
            print(board[i][j], end=" ")
        print("|")
    print("*-------*-------*-------*")


def solve_puzzle(board):
    """
    This function will solve the puzzle
    :param board: a 2D array that has the board
    :return: bool if found a salve
    """
    pos = find_empty_cell(board)
    if not pos:
        return True
    for i in range(1, 10):
        if check_num_valid(board, i, pos):
            board[pos[0]][pos[1]] = i
            if solve_puzzle(board):
                return True
            board[pos[0]][pos[1]] = 0
    return False


def write_solved_puzzle(file_name, board):
    """
    This function creates new file and saves the solved puzzle
    :param file_name: the file name of the unsolved puzzle
    :param board: the solved board
    :return: None
    """
    with open(file_name.split('.')[0] + "_solved.txt", 'w') as file:
        for row in board:
            for cell in row:
                file.write(str(cell) + " ")
            file.write("\n")


def main():
    file_name = 'puzzle.txt'
    board = load_puzzle(file_name)
    print("Unsolved")
    print_board(board)
    solve_puzzle(board)
    write_solved_puzzle(file_name, board)
    print("Solved")
    print_board(board)


if __name__ == "__main__":
    main()
