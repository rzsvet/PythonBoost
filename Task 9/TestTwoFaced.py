import unittest

from TwoFaced import TwoFaced


# Test cases to test Postmen methods
# You always create  a child class derived from unittest.TestCase
class TestFormation(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.twofaced = TwoFaced()

    # Each test method starts with the keyword test_
    def test_example_hi(self):
        self.assertEqual(self.twofaced.translator("Hi"), "дВулИкий дВУлИкиЙ")

    def test_example_123(self):
        self.assertEqual(self.twofaced.translator("123"), "двУЛикиЙ двУЛикИй двУЛикИЙ")

    def test_example_hello(self):
        result="ДВуЛикий ДвуЛИКИЙ ДВуЛикиЙ Двуликий ДВуЛикий ДвУЛИкий ДВуЛикий ДвУЛикИй ДВуЛикий ДвУЛиКиЙ ДВуЛикиЙ " \
               "ДвуликИй"
        self.assertEqual(self.twofaced.translator("Привет"), result)


if __name__ == "__main__":
    unittest.main()
