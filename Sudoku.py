import numpy as np

class Table:
    """
    A class to represent a state of the sudoku table, each cell has a value which can be 0 (empty cell) or 1-9, and a list of possible values
    value: a 9x9 np.ndarray table of cell values
    possible values: a queue of possible values for each cell"""

    def __init__(self):
        self.value = np.zeros((9, 9), dtype=np.int8)
        self.possible_values = self.__initializePossibleValues__()

    def __initializePossibleValues__(self):
        """ Initialize the possible values of each cell """
        return list(list(list(np.random.permutation(range(1, 10))) for _ in range(9)) for _ in range(9))
    
    """ def setPossibleValues(self, row, column):
        Set the possible values of a cell
        row: row of the cell
        column: column of the cell
        neighbors = self.neighbors(row, column)

        self.possible_values[row, column] =  """
    
    def initializeFromMatrix(self, matrix):
        """ Initialize the sudoku table from a matrix
        matrix: a 9x9 np.ndarray table of cell values """
        self.value = matrix
        self.possible_values = self.__initializePossibleValues__()

    def getEmptyCells(self):
        """
        Get the indices of an empty cell
        return: a list of indices of an empty cell
        """
        return [(i, j) for i in range(9) for j in range(9) if self.value[i, j] == 0]

    def popPossibleValue(self, row, column):
        """ Pop a possible value from the possible values of a cell
        row: row of the cell
        column: column of the cell
        return: the popped value """
        return self.possible_values[row][column].pop()
    
    def removePossibleValue(self, row, column, value):
        """ Remove a possible value from the possible values of a cell
        row: row of the cell
        column: column of the cell
        value: value to remove """
        self.possible_values[row][column].remove(value)
    
    def getPossibleValues(self, row, column):
        """ Get the possible values of a cell
        row: row of the cell
        column: column of the cell
        return: the possible values of the cell """
        return self.possible_values[row][column]

    def getBoxIndices(self, row, column):
        """ Get the indices of the box that contains the cell (row, column)
        row: row of the cell
        column: column of the cell
        return: a list of indices of the box that contains the cell (row, column) """
        return [(row // 3) * 3 + i for i in range(3)], [(column // 3) * 3 + i for i in range(3)]
    
    def neighbors(self, row, column):
        """ Get the indices of the cells which are in the same row, column or box of the cell (row, column)
        row: row of the cell
        column: column of the cell
        return: a list of indices of the cells which are in the same row, column or box of the cell (row, column) """
        row_indices = [i for i in range(9) if i != row]
        column_indices = [i for i in range(9) if i != column]
        box_row_indices, box_column_indices = self.getBoxIndices(row, column)
        return [(row, i) for i in column_indices] + [(i, column) for i in row_indices] + [(i, j) for i in box_row_indices for j in box_column_indices if (i, j) != (row, column)]

    def assign(self, row, column, value):
        """ Assign a value to a cell
        row: row of the cell
        column: column of the cell
        value: value to assign to the cell """
        self.value[row, column] = value

    def backtrackAssignment(self, row, column):
        """ Backtrack the assignment of a cell
        row: row of the cell
        column: column of the cell """
        self.value[row, column] = 0

    def isCellEmpty(self, row, column):
        """ Check if a cell is empty
        row: row of the cell
        column: column of the cell
        return: True if the cell is empty, False otherwise """
        return self.value[row, column] == 0
    
    def isCellCertain(self, row, column):
        """ Check if a cell is certain
        row: row of the cell
        column: column of the cell
        return: the value of the cell if the cell is certain, 0 otherwise """
        if (len(self.possible_values[row][column]) == 1):
            return self.possible_values[row][column][0]
        else:
            return 0

    def isComplete(self):
        """ Check if the sudoku table is complete
        return: True if the sudoku table is complete, False otherwise """
        return np.all(self.value != 0)
    


