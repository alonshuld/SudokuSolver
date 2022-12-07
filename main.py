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
            board.append((line.strip()).split(CHAR_SPLIT))
    return board


def main():
    file_name = 'puzzle.txt'
    print(load_puzzle(file_name))


if __name__ == "__main__":
    main()
