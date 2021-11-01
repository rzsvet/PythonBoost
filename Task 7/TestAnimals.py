import unittest

from Animals import Animals


# Test cases to test Postmen methods
# You always create  a child class derived from unittest.TestCase
class TestFormation(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.animals = Animals()

    # Each test method starts with the keyword test_
    def test_animals_2(self):
        result = self.animals.count_animals("goatcode")
        self.assertEqual(result, 2)

    def test_animals_4(self):
        result = self.animals.count_animals("cockdogwdufrbir")
        self.assertEqual(result, 4)

    def test_animals_5(self):
        result = self.animals.count_animals("dogdogdogdogdog")
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
