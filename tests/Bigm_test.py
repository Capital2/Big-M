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
        ip = np.matrix([ [1, 3, 3], [-2, 5, 1], [2, 8, 0], [-2, 2, 1] ])
        print(self.bm.runBigM(ip))

        
if __name__ == '__main__':
    unittest.main()