import unittest

question_03 = ''' Python script that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.'''


def min_max(number_sequence):
  
  x = number_sequence[0]
  y = number_sequence[0]
  a = number_sequence
  if(len(a)>1):
    for i in range(len(a)):
      if x>number_sequence[i]:
        x = number_sequence[i]
    for j in range(len(a)):
      if y<number_sequence[j]:
        y = number_sequence[j]
    return x,y
  else:
    return x
  pass
        


class TestMinMax(unittest.TestCase):
  def test_01(self):
    self.assertEqual(min_max((4,2,8,4,6)), (2,8))

  def test_02(self):
    self.assertEqual(min_max((4,2)), (2,4))
     
  def test_03(self):
    self.assertEqual(min_max((4,2,-8,4,6)), (-8, 6))
   
  def test_04(self):
    self.assertEqual(min_max((0,2,8,4,6)), (0,8))
    
  def test_05(self):
    self.assertEqual(min_max((2,2,2)), (2,2))
   
  def test_06(self):
    self.assertEqual(min_max((8,)), (8))

if _name_ == '_main_':
    unittest.main(verbosity=2)
