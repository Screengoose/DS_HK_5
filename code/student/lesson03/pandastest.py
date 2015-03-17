import sys
import numpy as np
import pandas as pd

matrix1 = [ [1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 0, 1, 2] ]

print np.matrix(matrix1)

df = pd.read_csv('nytimes.csv')
