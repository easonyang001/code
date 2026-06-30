from collections import deque


def bfs(graph: dict, start) -> list:
    """Breadth-first search; returns nodes in visit order."""
    visited = set()
    order = []
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order


def bfs_shortest_path(graph: dict, start, end) -> list | None:
    """Return shortest path from start to end, or None if unreachable."""
    if start == end:
        return [start]
    visited = {start}
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        for neighbour in graph.get(node, []):
            if neighbour == end:
                return path + [neighbour]
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])

    return None


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("BFS visit order from A:", bfs(graph, "A"))
    print("Shortest path A -> F:", bfs_shortest_path(graph, "A", "F"))

