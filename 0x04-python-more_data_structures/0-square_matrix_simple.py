def square_matrix_simple(matrix=[]):
    new = [[number**2 for number in row] for row in matrix]
    return new
