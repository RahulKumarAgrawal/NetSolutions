"""unittest."""
import unittest
import test1

class Test(unittest.TestCase):
    """we define our tests as methods.
    we add 1 tests/methods to test frequency of each elements in list."""
    def test_frequency(self):
        """we check if the result is what we want with parent class (TestCase) assertEqual method"""
        mylist = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
        result = test1.count_frequency(mylist)
        self.assertEqual(result, {1: 3, 2: 4, 3: 4, 4: 2, 5: 1})

if __name__ == '__main__':
    unittest.main()
