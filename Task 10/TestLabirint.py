import unittest

from Labirint import Labirint


# Test cases to test Postmen methods
# You always create  a child class derived from unittest.TestCase
class TestFormation(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.labirint = Labirint()

    # Each test method starts with the keyword test_
    def test_example_one(self):
        self.assertTrue(self.labirint.can_exit([
          [0, 1, 1, 1, 1, 1, 1],
          [0, 0, 1, 1, 0, 1, 1],
          [1, 0, 0, 0, 0, 1, 1],
          [1, 1, 1, 1, 0, 0, 1],
          [1, 1, 1, 1, 1, 0, 0]
        ]))

    def test_example_two(self):
        self.assertFalse(self.labirint.can_exit([
          [0, 1, 1, 1, 1, 1, 1],
          [0, 0, 1, 0, 0, 1, 1],
          [1, 0, 0, 0, 0, 1, 1],
          [1, 1, 0, 1, 0, 0, 1],
          [1, 1, 0, 0, 1, 1, 1]
        ]))

    def test_example_three(self):
        self.assertFalse(self.labirint.can_exit([
          [0, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 0, 0],
          [1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1]
        ]))

    def test_example_four(self):
        self.assertTrue(self.labirint.can_exit([
          [0, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 0, 0],
          [1, 1, 1, 0, 0, 0, 0],
          [1, 0, 0, 0, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 0]
        ]))



if __name__ == "__main__":
    unittest.main()
