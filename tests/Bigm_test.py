import unittest
from mock import patch
# Tested class
from BigM import BigM
import numpy as np


class TestIH(unittest.TestCase):

    def setUp(self) -> None:
        self.bm = BigM.BigM()
        return super().setUp()

    def test_run_bigm(self):
        tests = [np.matrix([[1, 1, 0, 1], [1, 0, 1, -1], [0, 1, 1, 3],[20, 5, 10, 0], [-2, 0, 2, 0]]),
                np.matrix([ [3, 1, 1, 200], [2, 2, 1, 300], [600, 400, 225, 0], [0, -2, -2, 0] ]),
                np.matrix([ [4, 1, 0, 3], [1, 1, 1, 2], [1, 0, 1, 6], [100, 40, 30, 0], [-2, 2, -2, 0] ]),
                np.matrix([ [3, 4, 1, -4], [-1, 20, -1, 3], [1, -1, 1, 1], [40, 1, 5, 0], [-2, 0, 2, 0] ]),
                np.matrix([ [5, 7, 1, -4], [-2, 200, -3, -9], [2, -1, -2, -2], [40, 1, 5, 0], [-2, 0, 0, 0] ])]
        for test in tests:
            try:
                self.bm.runBigM(test)
                # TODO assert dominance ha
            except Exception as error:
                print(error)
        
if __name__ == '__main__':
    unittest.main()