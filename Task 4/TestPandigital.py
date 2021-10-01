import unittest

from Pandigital import Pandigital


# Test cases to test Pandigital methods
# You always create  a child class derived from unittest.TestCase
class TestFormation(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.pandigital = Pandigital()

    # Each test method starts with the keyword test_
    def test_pandigital_true(self):
        self.assertTrue(self.pandigital.is_pandigital(98140723568910))

    def test_pandigital_false_one(self):
        self.assertFalse(self.pandigital.is_pandigital(90864523148909))

    def test_pandigital_false_two(self):
        self.assertFalse(self.pandigital.is_pandigital(112233445566778899))


if __name__ == "__main__":
    unittest.main()
