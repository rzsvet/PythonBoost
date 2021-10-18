import unittest

from Postmen import Postmen


# Test cases to test Postmen methods
# You always create  a child class derived from unittest.TestCase
class TestFormation(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.postmen = Postmen()

    # Each test method starts with the keyword test_
    def test_matrix_2x2(self):
        result = self.postmen.harry([[5, 2], [5, 2]])
        self.assertEqual(result, 12)

    def test_matrix_3x5(self):
        result = self.postmen.harry([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15]
        ])
        self.assertEqual(result, 72)

    def test_matrix_0x0(self):
        result = self.postmen.harry([[]])
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
