def merge_and_filter_unique(lst1: list[int], lst2: list[int]) -> list[int]:
    """
    Merges two lists, removes duplicates, and returns the first 3 unique elements.
    
    Interpretation 1: Remove duplicate values from merged list.
    This keeps one copy of each value.
    Args:
        lst1 (list[int]): First input list.
        lst2 (list[int]): Second input list.

    Returns:
        list[int]: First 3 elements of the deduplicated merged list.
    """
    merged = lst1 + lst2
    unique = list(dict.fromkeys(merged))  # keep order + remove duplicates
    return unique[:3]


if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [4, 5, 6, 7, 8]
    result = merge_and_filter_unique(list_1, list_2)
    print(result)  # ➜ [1, 2, 3]
