def square_matrix_simple(matrix=[]):
    newone = []
    for row in matrix :
        row1 = []
        for n in row :
            row1.append(n **2)
            newone.append(row1)
    return newone
