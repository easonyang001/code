def dfs_iterative(graph: dict, start) -> list:
    """Depth-first search (iterative); returns nodes in visit order."""
    visited = set()
    order = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in visited:
                stack.append(neighbour)

    return order


def dfs_recursive(graph: dict, start, visited: set = None, order: list = None) -> list:
    """Depth-first search (recursive); returns nodes in visit order."""
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(start)
    order.append(start)
    for neighbour in graph.get(start, []):
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited, order)

    return order


def dfs_has_path(graph: dict, start, end, visited: set = None) -> bool:
    """Return True if there is a path from start to end."""
    if visited is None:
        visited = set()
    if start == end:
        return True
    visited.add(start)
    for neighbour in graph.get(start, []):
        if neighbour not in visited:
            if dfs_has_path(graph, neighbour, end, visited):
                return True
    return False


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("DFS iterative from A:", dfs_iterative(graph, "A"))
    print("DFS recursive from A:", dfs_recursive(graph, "A"))
    print("Path exists A -> F:", dfs_has_path(graph, "A", "F"))
    print("Path exists D -> C:", dfs_has_path(graph, "D", "C"))
