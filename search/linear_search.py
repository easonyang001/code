def linear_search(arr: list, target) -> int:
    """Return index of target in arr, or -1 if not found."""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


if __name__ == "__main__":
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    target = 9
    idx = linear_search(data, target)
    if idx != -1:
        print(f"Found {target} at index {idx}")
    else:
        print(f"{target} not found")
