import unittest

# Tested class
import service.BigM as bm

class TestBigM(unittest.TestCase):
    exampleConsTrue = ["3x+y=1", "x-Y>=0", " x +  50y<6 ", "y<5", "   x+y-z>0 "]
    exampleObjectiveTrue = ["Max Z = 3x+y", "mIn z= 2x-y", " Min z =3x +50y - z    ", "maX Z = x+y", "MAX z = 50x+2000y", "Max j = 3x + y"]

    exampleConsFalse = ["3x>==1", "x +x +y< 1", "x * y > 3", "ax + 5b < 2", "x + y >3z", "x>z", "x +>2"]
    exampleObjectiveFalse = [" z = 3x+y ", "m z = 3x+y", " = 3x + y", "Max Z = 3x +"]

    def test_validateUserInput(self):
        for t in (self.exampleObjectiveTrue + self.exampleConsTrue):
            tested = bm.BigM.validateUserInput(t)
            self.assertTrue(tested)

        for t in (self.exampleObjectiveFalse + self.exampleConsFalse):
            tested = bm.BigM.validateUserInput(t)
            self.assertFalse(tested)

if __name__ == '__main__':
    unittest.main()