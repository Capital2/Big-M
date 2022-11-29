import unittest
from mock import patch
import numpy as np
# Tested class

from BigM import InputHandling, graph
class TestIH(unittest.TestCase):

    def setUp(self) -> None:
        self.exampleConsTrue = ["3x+y=1", "x-Y>=0", " x +  50y<6 ", "   x+y-z>0 ", "y<0"]
        self.exampleObjectiveTrue = ["Max Z = 3x+y", "mIn z= 2x-y", " Min j =3x +50y - z    ", "maX w = x+y", "MAX z = 50x+2000y", "Max j = 3x + y"]

        self.exampleConsFalse = ["3x>==1", "x +x +y< 1", "x * y > 3", "ax + 5b < 2", "x + y >3z", "x>z", "x +>2", "-z-3x+5y6", "y+x5"]
        self.exampleObjectiveFalse = [" z = 3x+y ", "m z = 3x+y", " = 3x + y", "Max Z = 3x +"]
        return super().setUp()

    def test_validateUserInput(self):
        for t in (self.exampleObjectiveTrue + self.exampleConsTrue):
            tested = InputHandling.validateUserInput(t)
            self.assertTrue(tested,f"{t} should be true")

        for t in (self.exampleObjectiveFalse + self.exampleConsFalse):
            tested = InputHandling.validateUserInput(t)
            self.assertFalse(tested,f"{t} should be false")
    
    def test_formatUserInput(self):
        testcase1 = (["Max Z = 3x+y","x-2y<=2","3x+5y>=8"], [ [1, 3, 3], [-2, 5, 1], [2, 8, 0], [-2, 2, 1] ])
        testcase2 = (["Min Z = 3x+y+2z","x-2y-z<2","3x+5y+50z>8"], [ [1, 3, 3], [-2, 5, 1], [-1, 50, 2], [2, 8, 0], [-1, 1, -1] ])
        testcase3 = (["Max Z = 3x+y+2z","x-z=2","5y+50z>8", "z>=0"], [ [1, 0, 0, 3], [0, 5, 0, 1], [-1, 50, 1, 2], [2, 8, 0, 0], [0, 1, 2, 1] ])
        testcase4 = (["Max Z = x-3y", "3y-x = 5", "-y+3x < -1"], [ [-1, 3, 1], [3, -1, -3], [5, -1, 0], [0, -1, 1] ])

        self.assertEqual(InputHandling.formatUserInput(testcase1[0]), testcase1[1])
        self.assertEqual(InputHandling.formatUserInput(testcase2[0]), testcase2[1])
        self.assertEqual(InputHandling.formatUserInput(testcase3[0]), testcase3[1])
        self.assertEqual(InputHandling.formatUserInput(testcase4[0]), testcase4[1])

    def test_drawGraph(self):
        tests = [np.array([[1, 1, 0, 1], [1, 0, 1, -1], [0, 1, 1, 3],[20, 5, 10, 0], [-2, 0, 2, 0]]),
        np.array([ [3, 1, 1, 200], [2, 2, 1, 300], [600, 400, 225, 0], [0, -2, -2, 0] ]),
        np.array([ [4, 1, 0, 3], [1, 1, 1, 2], [1, 0, 1, 6], [100, 40, 30, 0], [-2, 2, -2, 0] ]),
        np.array([ [3, 4, 1, -4], [-1, 20, -1, 3], [1, -1, 1, 1], [40, 1, 5, 0], [-2, 0, 2, 0] ]),
        np.array([ [5, 7, 1, -4], [-2, 200, -3, -9], [2, -1, -2, -2], [40, 1, 5, 0], [-2, 0, 0, 0] ])]
        # A way of testing the draw func, is that we test whether the show function have been
        # called or not relying on the fact that the show() func is usually called at the end of 
        # the drawGraph func.
        with patch("matplotlib.pyplot.show") as show_patch:
            for test in tests:
                graph.drawGraph(test)
                show_patch.assert_called()
    
if __name__ == '__main__':
    unittest.main()