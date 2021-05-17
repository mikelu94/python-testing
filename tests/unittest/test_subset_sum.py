import unittest

from src import subset_sum


class TestSubsetSum(unittest.TestCase):

    def test_exists_subset_sum(self):
        self.assertTrue(subset_sum([1, 2, 3, 4, 5], 15))

    def test_not_exists_subset_sum(self):
        self.assertFalse(subset_sum([1, 2, 3, 4, 5], 16))

    def test_zero_subset_sum(self):
        self.assertTrue(subset_sum([], 0))
