import unittest

from src import topological_sort


class TestTopologicalSort(unittest.TestCase):

    def test_topological_sort(self):
        dag = {
            0: [1, 2, 3, 4, 5],
            1: [2, 3, 4, 5],
            2: [3, 4, 5],
            3: [4, 5],
            4: [5],
            5: []
        }
        self.assertEquals(topological_sort(dag), [0, 1, 2, 3, 4, 5])

    def test_topological_sort_trivial_dag(self):
        trivial_dag = {}
        self.assertEqual(topological_sort(trivial_dag), [])
