from src import cycle_detection


def test_acyclic():
    acyclic_graph = {
        0: [],
        1: [0],
        2: [1],
    }
    assert cycle_detection(acyclic_graph) is False


def test_cyclic():
    cyclic_graph = {
        0: [2],
        1: [0],
        2: [1],
    }
    assert cycle_detection(cyclic_graph) is True
