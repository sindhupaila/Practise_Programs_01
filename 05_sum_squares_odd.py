import unittest

question_05 = ''' Python script that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.'''


def sum_squares_odd(n):
  pass
        


class TestSumSquaresOdd(unittest.TestCase):
  def test_01(self):
    self.assertEqual(sum_squares_odd(4), 10)

  def test_02(self):
    self.assertEqual(sum_squares_odd(9), 84)
     
  def test_03(self):
    self.assertEqual(sum_squares_odd(1), 0)
   
  def test_04(self):
    self.assertEqual(sum_squares_odd(2), 1)
    
  def test_05(self):
    self.assertEqual(sum_squares(100), 166650)
  
if __name__ == '__main__':
    unittest.main(verbosity=2)
