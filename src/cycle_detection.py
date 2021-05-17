from queue import Queue
from typing import Any

_Graph = dict[Any, list[Any]]


def cycle_detection(graph: _Graph) -> bool:
    """Calculate whether a graph has a cycle"""
    return len(graph) != len(topological_sort(graph))


# Kahn's Algorithm
def topological_sort(graph: _Graph) -> list[Any]:
    """Calculate the topological sort of a DAG"""
    nodes = set(graph)
    in_degree = {node: 0 for node in nodes}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    queue = Queue()
    for node in nodes:
        if not in_degree[node]:
            queue.put(node)
    TS = []
    while not queue.empty():
        node = queue.get()
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if not in_degree[neighbor]:
                queue.put(neighbor)
        TS.append(node)
    return TS
