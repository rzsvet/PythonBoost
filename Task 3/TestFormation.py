import unittest

from Formation import Formation


# Test cases to test Formation methods
# You always create  a child class derived from unittest.TestCase
class TestFormation(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.formation = Formation()

    # Each test method starts with the keyword test_
    def test_stalactites(self):
        result = self.formation.mineralFormation([
            [0, 1, 0, 1],
            [0, 1, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 0]
        ])
        self.assertEqual(result, "stalactites")

    def test_stalagmites(self):
        result = self.formation.mineralFormation([
            [0, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 1, 1, 1],
            [0, 1, 1, 1]
        ])
        self.assertEqual(result, "stalagmites")

    def test_both(self):
        result = self.formation.mineralFormation([
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [0, 1, 1, 1],
            [0, 1, 1, 1]
        ])
        self.assertEqual(result, "both")

    def test_none(self):
        result = self.formation.mineralFormation([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])
        self.assertEqual(result, "none")


if __name__ == "__main__":
    unittest.main()
