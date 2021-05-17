import unittest

from src import cycle_detection


class TestCycleDetection(unittest.TestCase):

    def test_acyclic(self):
        acyclic_graph = {
            0: [],
            1: [0],
            2: [1],
        }
        self.assertFalse(cycle_detection(acyclic_graph))

    def test_cyclic(self):
        cyclic_graph = {
            0: [2],
            1: [0],
            2: [1],
        }
        self.assertTrue(cycle_detection(cyclic_graph))
