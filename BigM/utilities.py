import numpy as np


class Utilities:

    @staticmethod
    def get_col_index(matrix: np.matrix, i: int) -> int:
        ix = -1
        for j in range(0, matrix.shape[1]):
            if matrix.item(i, j) != 0:
                ix = j
                break
        return ix

    @staticmethod
    def handle_type_detection(x: any):
        if type(x) == str:
            x = x[1: len(x)]
            return float(x) * -1
        else:
            return x

    @staticmethod
    def debug(entity: any, msg: str = None):
        print()
        if msg != None:
            print(msg)
        print(entity)
        print("*************************************")
        input('press any key to continue.')
        print()


equation_type_converter = {
    1: -2,
    2: -1,
    -1: 2,
    -2: 1,
    0: 0
}
