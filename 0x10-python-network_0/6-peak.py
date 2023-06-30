#!/usr/bin/python3

# a function that finds a peak in a list of unsorted integers.

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): The list of unsorted integers.

    Returns:
        int or None: The peak element if found, or None if the list is empty.

    """
    # If the list is empty, return None.
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    mid = length // 2
    arr = list_of_integers

    # Check if the middle element is a peak
    if (mid - 1 < 0 and mid + 1 >= length):
        return arr[mid]

    # If the right neighbor is greater, search in the right subarray
    elif mid - 1 < 0:
        return arr[mid] if arr[mid] >arr[mid + 1] else arr[mid + 1]

    elif mid + 1 >= length:
        return arr[mid] if arr[mid] > arr[mid - 1] else arr[mid - 1]

    if arr[mid -1] < arr[mid] > arr[mid + 1]:
        return arr[mid]

    if arr[mid + 1] > arr[mid - 1]:
        return find_peak(arr[mid:])

    # If the left neighbor is greater, search in the left subarray
    return find_peak(arr[:mid])

