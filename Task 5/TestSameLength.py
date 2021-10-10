import unittest

from SameLength import SameLength


# Test cases to test SameLength methods
# You always create  a child class derived from unittest.TestCase
class TestFormation(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.func = SameLength()

    # Each test method starts with the keyword test_
    def test_same_length_true_first(self):
        self.assertTrue(self.func.same_length(110011100010))

    def test_same_length_false_first(self):
        self.assertFalse(self.func.same_length(101010110))

    def test_same_length_true_second(self):
        self.assertTrue(self.func.same_length(111100001100))

    def test_same_length_false_second(self):
        self.assertFalse(self.func.same_length(111))


if __name__ == "__main__":
    unittest.main()
