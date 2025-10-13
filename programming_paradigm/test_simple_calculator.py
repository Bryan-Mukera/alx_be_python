import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

  def setUp(self):
    """Set up the SimpleCalculator instance before each test."""
    self.calc = SimpleCalculator()

  def addition(self):
    self.assertEqual(self.calc.add(2, 3), 5)
    self.assertEqual(self.calc.add(-1, 1), 0)

  def subtration(self):
    self.assertEqual(self.calc.subtract(3,2), 1)
    self.assertEqual(self.calc.subtract(1,-1), 2)

  def division(self):
    self.assertEqual(self.calc.divide(6,2), 3)
    self.assertEqual(self.calc.divide(1, 0), None)