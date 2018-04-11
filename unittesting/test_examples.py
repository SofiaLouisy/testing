import unittest


class NumberTest(unittest.TestCase):
    """
    Uses subtest to display all tests within a test method
    """
    def test_even_numbers(self):
        """
        with subtest, all failures are shown
        """
        for i in range(10):
            with self.subTest(i=i):
                self.assertEqual(i % 2,0)

    def test_even_numbers_again(self):
        """
        without subtest, only first failure is shown
        """
        for i in range(10):
            self.assertEqual(i % 2,0)