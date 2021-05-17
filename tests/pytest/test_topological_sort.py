from src import topological_sort


def test_topological_sort():
    dag = {
        0: [1, 2, 3, 4, 5],
        1: [2, 3, 4, 5],
        2: [3, 4, 5],
        3: [4, 5],
        4: [5],
        5: []
    }
    assert topological_sort(dag) == [0, 1, 2, 3, 4, 5]


def test_topological_sort_trivial_dag():
    trivial_dag = {}
    assert topological_sort(trivial_dag) == []
