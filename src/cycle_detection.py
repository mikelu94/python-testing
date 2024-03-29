"""Module for detecting cycles in directed graphs."""
from collections.abc import Mapping, Sequence
from queue import Queue
from typing import Any, List

_Graph = Mapping[Any, Sequence[Any]]


def cycle_detection(graph: _Graph) -> bool:
    """Calculate whether a directed graph has a cycle."""
    return len(graph) != len(topological_sort(graph))


# Kahn's Algorithm
def topological_sort(graph: _Graph) -> List[Any]:
    """Calculate the topological sort of a DAG."""
    nodes = set(graph)
    in_degree = {node: 0 for node in nodes}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    queue: Queue = Queue()
    for node in nodes:
        if not in_degree[node]:
            queue.put(node)
    topological_sort_order = []
    while not queue.empty():
        node = queue.get()
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if not in_degree[neighbor]:
                queue.put(neighbor)
        topological_sort_order.append(node)
    return topological_sort_order
