import Sudoku
import numpy as np

def generate_sudoku():
    """
    Generate a sudoku table from some examples taken from the Internet
    """
    sudoku = Sudoku.Table()
    """ matrix = np.array([[0, 0, 0, 2, 6, 0, 7, 0, 1],
                          [6, 8, 0, 0, 7, 0, 0, 9, 0],
                          [1, 9, 0, 0, 0, 4, 5, 0, 0],
                          [8, 2, 0, 1, 0, 0, 0, 4, 0],
                          [0, 0, 4, 6, 0, 2, 9, 0, 0],
                          [0, 5, 0, 0, 0, 3, 0, 2, 8],
                          [0, 0, 9, 3, 0, 0, 0, 7, 4],
                          [0, 4, 0, 0, 5, 0, 0, 3, 6],
                          [7, 0, 3, 0, 1, 8, 0, 0, 0]]) """
    matrix = np.zeros((9, 9), dtype=np.int8)
    matrix[0, 3] = 6
    matrix[0, 6] = 8 
    matrix[1, 2] = 9 
    matrix[2, 1] = 5 
    matrix[3, 1] = 7 
    matrix[3, 7] = 5 
    matrix[3, 8] = 9 
    matrix[4, 3] = 8
    matrix[4, 8] = 4 
    matrix[5, 0] = 6 
    matrix[5, 7] = 3
    matrix[6, 0] = 1
    matrix[6, 6] = 2
    matrix[7, 0] = 7
    matrix[7, 4] = 9
    matrix[8, 3] = 4
    matrix[8, 4] = 5
    sudoku.initializeFromMatrix(matrix)
    return sudoku