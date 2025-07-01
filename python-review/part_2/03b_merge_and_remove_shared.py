def merge_and_remove_common(lst1: list[int], lst2: list[int]) -> list[int]:
    """
    Merges two lists, removes all values that are common between them,
    and returns the first 3 unique elements from the filtered result.
    
    Interpretation 2: Remove all values that appear in both lists.
    No shared values will remain in the result.
    Args:
        lst1 (list[int]): First input list.
        lst2 (list[int]): Second input list.

    Returns:
        list[int]: The first 3 elements after removing shared values.
    """
    common = set(lst1) & set(lst2)
    combined = lst1 + lst2
    filtered = [item for item in combined if item not in common]
    return filtered[:3]



if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [4, 5, 6, 7, 8]
    result = merge_and_remove_common(list_1, list_2)
    print(result)
