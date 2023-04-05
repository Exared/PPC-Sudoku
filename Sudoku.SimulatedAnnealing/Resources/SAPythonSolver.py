#instance = ((0,0,0,0,9,4,0,3,0),
#           (0,0,0,5,1,0,0,0,7),
#           (0,8,9,0,0,0,0,4,0),
#           (0,0,0,0,0,0,2,0,8),
#           (0,6,0,2,0,1,0,5,0),
#           (1,0,2,0,0,0,0,0,0),
#           (0,7,0,0,0,0,5,2,0),
#           (9,0,0,0,6,5,0,0,0),
#           (0,4,0,9,7,0,0,0,0))
def find_empty_location(puzzle):
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    return row, col
        return None


def is_valid(puzzle, row, col, num):
        # check row
        for i in range(9):
            if puzzle[row][i] == num:
                return False
        # check column
        for i in range(9):
            if puzzle[i][col] == num:
                return False
        # check square
        square_row = (row // 3) * 3
        square_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if puzzle[square_row + i][square_col + j] == num:
                    return False
        return True


def solveSudoku(board):
    """
    Solves a Sudoku puzzle using a recursive backtracking algorithm.

    Args:
    - board: 2D list representing the Sudoku board.

    Returns:
    - True if a solution is found, False otherwise.
    """
    # Find the next empty cell
    row, col = findEmptyCell(board)
    
    # If there are no empty cells, the board is solved
    if row == -1 and col == -1:
        return True
    
    # Try all numbers from 1 to 9 in the empty cell
    for num in range(1, 10):
        # Check if the number is valid in the current cell
        if isValid(board, row, col, num):
            # If the number is valid, set it in the current cell
            board[row][col] = num
            
            # Recursively solve the updated board
            if solveSudoku(board):
                return True
            
            # If a solution is not found, backtrack by resetting the current cell
            board[row][col] = 0
            
    # If no valid number is found, backtrack
    return False


#start = default_timer()
if(solveSudoku(instance)):
	#print_grid(instance)
	r=instance
else:
	print ("Aucune solution trouvée")

#execution = default_timer() - start
#print("Le temps de résolution est de : ", execution, " seconds as a floating point value")