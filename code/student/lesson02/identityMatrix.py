import numpy as np

def identityMatrix(rows):

    '''
    Create an empty matrix list
    Append new rows of 0s to the list, with the number of elements dependent on the number of rows
    Substitute a 1 for a 0 in the place of matrix[x][x]
    Use numpy to pretify it

    Interesting note:
    Just doing "matrix = [[0] * size] * size" does not work for creating the matrix filled with 0s (although it seems like it should)
    Not completely sure why.  Seems that every element is referenced as the SAME element.
    Would love an explanation as to why this is.
    '''

    matrix = []
    for x in range(rows):
        matrixRow = [0] * rows
        matrix.append(matrixRow)

    for x in range(rows):
        matrix[x][x] = 1

    print np.matrix(matrix)

identityMatrix(10)
