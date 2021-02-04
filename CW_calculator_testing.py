import unittest
import CW_Calculator_NoInput

class TestCaseAddition(unittest.TestCase):
    def test1(self):
        self.assertEqual(CW_Calculator_NoInput.addition(1,1),2)
    def test2(self):
        self.assertEqual(CW_Calculator_NoInput.addition(-3,-4),-7)
    def test3(self):
        self.assertEqual(CW_Calculator_NoInput.addition(1.5,3),4.5)
    def test4(self):
        self.assertEqual(CW_Calculator_NoInput.addition(-3,4),1)

class TestCaseSubtraction(unittest.TestCase):
    def test1(self):
        self.assertEqual(CW_Calculator_NoInput.subtraction(1,1),0)
    def test2(self):
        self.assertEqual(CW_Calculator_NoInput.subtraction(-3,-4),1)
    def test3(self):
        self.assertEqual(CW_Calculator_NoInput.subtraction(1.5,2.5),-1)
    def test4(self):#will fail on purpose
        self.assertEqual(CW_Calculator_NoInput.subtraction(1,-2),-1)

class TestCaseMultiplication(unittest.TestCase):
    def test1(self):
        self.assertEqual(CW_Calculator_NoInput.multiplication(1,1),1)
    def test2(self):
        self.assertEqual(CW_Calculator_NoInput.multiplication(-3,-4),12)
    def test3(self):
        self.assertEqual(CW_Calculator_NoInput.multiplication(1,2.5),2.5)
    def test4(self):
        self.assertEqual(CW_Calculator_NoInput.multiplication(1,-2),-2)

class TestCaseDivision(unittest.TestCase):
    def test1(self):
        self.assertEqual(CW_Calculator_NoInput.division(1,1),1)
    def test2(self):
        self.assertEqual(CW_Calculator_NoInput.division(-12,-4),3)
    def test3(self):
        self.assertEqual(CW_Calculator_NoInput.division(2.5,1),2.5)
    def test4(self): #Will fail on purpose per the return value of division not being zero due to "y" being zero
        self.assertEqual(CW_Calculator_NoInput.division(1,0),0)

if __name__ == "__main__": #Using this line from the unittest lecture to display the number of failures in the test
    unittest.main(verbosity=2)