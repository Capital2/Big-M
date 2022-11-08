import unittest

# Tested class
import service.BigM as bm

class TestBigM(unittest.TestCase):

    def setUp(self) -> None:
        self.exampleConsTrue = ["3x+y=1", "x-Y>=0", " x +  50y<6 ", "   x+y-z>0 "]
        self.exampleObjectiveTrue = ["Max Z = 3x+y", "mIn z= 2x-y", " Min j =3x +50y - z    ", "maX w = x+y", "MAX z = 50x+2000y", "Max j = 3x + y"]

        self.exampleConsFalse = ["3x>==1", "x +x +y< 1", "x * y > 3", "ax + 5b < 2", "x + y >3z", "x>z", "x +>2", "y<0"]
        self.exampleObjectiveFalse = [" z = 3x+y ", "m z = 3x+y", " = 3x + y", "Max Z = 3x +"]
        return super().setUp()

    def test_validateUserInput(self):
        for t in (self.exampleObjectiveTrue + self.exampleConsTrue):
            tested = bm.BigM.validateUserInput(t)
            self.assertTrue(tested,f"{t} should be true")

        for t in (self.exampleObjectiveFalse + self.exampleConsFalse):
            tested = bm.BigM.validateUserInput(t)
            self.assertFalse(tested,f"{t} should be false")
    
    def test_formatUserInput(self):
        testcase = (["Max Z = 3x+y","x-2y<=2","3x+5y>=8"], [ [1, 3, 3], [-2, 5, 1], [2, 8, 0], [-1, 1, 1] ])
        self.assertEqual(bm.BigM.formatUserInput(testcase[0]), testcase[1])

if __name__ == '__main__':
    unittest.main()