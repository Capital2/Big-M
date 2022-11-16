import numpy as np;

class Utilities:
    
    @staticmethod
    def get_col_index(matrix: np.matrix, i: int) -> int:
        ix = -1
        for j in range(0, matrix.shape[1]):
            if matrix.item(i, j) != 0:
                ix = j
                break
        return ix
