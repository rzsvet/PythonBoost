import unittest

from Minesweeper import Minesweeper


# Test cases to test Postmen methods
# You always create  a child class derived from unittest.TestCase
class TestFormation(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.minesweeper = Minesweeper()

    # Each test method starts with the keyword test_
    def test_example_01(self):
        result = self.minesweeper.num_grid([
          ["-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-"],
          ["-", "-", "#", "-", "-"],
          ["-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-"]
        ])
        self.assertEqual(result, [
          ["0", "0", "0", "0", "0"],
          ["0", "1", "1", "1", "0"],
          ["0", "1", "#", "1", "0"],
          ["0", "1", "1", "1", "0"],
          ["0", "0", "0", "0", "0"],
        ])
    def test_example_02(self):
        result = self.minesweeper.num_grid([
          ["-", "-", "-", "-", "#"],
          ["-", "-", "-", "-", "-"],
          ["-", "-", "#", "-", "-"],
          ["-", "-", "-", "-", "-"],
          ["#", "-", "-", "-", "-"]
        ])
        self.assertEqual(result, [
          ["0", "0", "0", "1", "#"],
          ["0", "1", "1", "2", "1"],
          ["0", "1", "#", "1", "0"],
          ["1", "2", "1", "1", "0"],
          ["#", "1", "0", "0", "0"]
        ])
    def test_example_03(self):
        result = self.minesweeper.num_grid([
          ["-", "-", "-", "#", "#"],
          ["-", "#", "-", "-", "-"],
          ["-", "-", "#", "-", "-"],
          ["-", "#", "#", "-", "-"],
          ["-", "-", "-", "-", "-"]
        ])
        self.assertEqual(result, [
          ["1", "1", "2", "#", "#"],
          ["1", "#", "3", "3", "2"],
          ["2", "4", "#", "2", "0"],
          ["1", "#", "#", "2", "0"],
          ["1", "2", "2", "1", "0"],
        ])


if __name__ == "__main__":
    unittest.main()
