import numpy as np

# Define matrix and vector
vector = [1, 2, 3, 4]
matrix = [ [1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 0, 1, 2] ]

# Function 1
def vectorMatrixMultiplication(matrix,vector):
    """
    Iterate over matrix rows with for loop
    Set an answer variable
    For each vector, multiply vector by corresponding matrix integer in row
    Sum the resulting 4 outputs of the row
    Set answer equal to output
    """
    answerList = []
    for x in range(len(matrix)):
        answer = 0
        for y in range(len(vector)):
            answer = answer + vector[y] * matrix[x][y]
        answerList.append(answer)
    print answerList


# Function 2
def matrixMutiplication(matrix1, matrix2):
    """
    Same methodology as above
    One additional loop required to iterate over the second matrix rows
    """
    answerMatrix=[]
    for x in range(len(matrix1)):
        answerList = []
        for y in range(len(matrix2)):
            answer = 0
            for z in range(len(matrix2[y])):
                answer = answer + matrix2[y][z] * matrix2[x][z]
            answerList.append(answer)
        answerMatrix.append(answerList)

    print np.matrix(answerMatrix)

# Call functions
vectorMatrixMultiplication(matrix,vector)
matrixMutiplication(matrix, matrix)
