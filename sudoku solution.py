def check_sudoku_board(board):
    """
    Checks the state of the sudoku board passed in as `board`.
    If the board has an error of any kind (ie a repeated numer in any row,
    column, or 3x3 block), then the return value will be "Error in X x Y" where
    X and Y are the coordinates of cell with the duplicate.
    
    If the board has no errors but has blanks (ie empty strings), then the
    return value will "Incomplete".
    
    If the board has no errors and no blanks, then the return value will be
    "Complete".
    """    
    # 1. Check for duplicates in each row
    for y in range(9):
        for i in range(1, 10):
            if  board[y].count(i) > 1:
                return f"Error in {board[y].index(i) + 1} x {y + 1}"
    # 2. Check for duplicates in each col
    for x in range(9):
        col = [board[y][x] for y in range(9)]
        for i in range(1, 10):
            if  col.count(i) > 1:
                return f"Error in {x + 1} x {col.index(i) + 1}"
    # 3. Check for duplicates in each 3x3 block
    for block_x in range(3):
        for block_y in range(3):
            values = []
            coords = []
            for x in range(block_x * 3, block_x * 3 + 3):
                for y in range(block_y * 3, block_y * 3 + 3):
                    values.append(board[y][x])
                    coords.append((x + 1, y + 1))
            for i in range(1, 10):
                if values.count(i) > 1:
                    x, y = coords[values.index(i)]
                    return f"Error in {x} x {y}"
    # 4. Check for empties
    for row in board:
        for cell in row:
            if cell == '':
                return "Incomplete"
        
    # If we found neither an error nor empty, the board is complete.
    return "Complete."

def print_sudoku_board(board):
    for y in range(9):
        for x in range(9):
            print(f"{board[y][x]:1}", end='')
            if x == 2 or x == 5:
                print('|', end='')
            else:
                print(' ', end='')
        print()
        if y == 2 or y == 5:
            print('-----+-----+-----')

if __name__ == "__main__":
    board = [
        [4, 3, 5, 2, 6, 9, 7, 8, 1],
        [6, 8, 2, 5, 7, 1, 4, 9, 3],
        [1, 9, 7, 8, 3, 4, 5, 6, 2],
        [8, 2, 6, 1, 9, 5, 3, 4, 7],
        [3, 7, 4, 6, 8, 2, 9, 1, 5],
        [9, 5, 1, 7, 4, 3, 6, 2, 8],
        [5, 1, 9, 3, 2, 6, 8, 7, 4],
        [2, 4, 8, 9, 5, 7, 1, 3, 6],
        [7, 6, 3, 4, 1, 8, 2, 5, 9],
    ]
    print_sudoku_board(board)
    print(check_sudoku_board(board))
    board = [
        ['', 3, '', '', '', '', '', '', ''],
        ['', 3, '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
    ]
    print_sudoku_board(board)
    print(check_sudoku_board(board))
