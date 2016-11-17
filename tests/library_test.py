import unittest

import example

class LibraryTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_another(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

    def test_fizz_buzz(self):
        self.assertEqual(example.fizz_buzz(2),'2')
        self.assertEqual(example.fizz_buzz(3),'Fizz')


if __name__ == '__main__':
    unittest.main()
