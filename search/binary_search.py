def binary_search(arr: list, target) -> int:
    """Return index of target in a sorted arr, or -1 if not found."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_recursive(arr: list, target, lo: int = 0, hi: int = None) -> int:
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)
    else:
        return binary_search_recursive(arr, target, lo, mid - 1)


if __name__ == "__main__":
    data = sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    print(f"Sorted array: {data}")

    target = 6
    print(f"Iterative: index of {target} = {binary_search(data, target)}")
    print(f"Recursive: index of {target} = {binary_search_recursive(data, target)}")
