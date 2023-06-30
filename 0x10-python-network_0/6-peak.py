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
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and \
            (mid == length - 1 or arr[mid + 1] <= arr[mid]):
        return arr[mid]

    # If the right neighbor is greater, search in the right subarray
    if mid < length - 1 and arr[mid + 1] > arr[mid]:
        return find_peak(arr[mid + 1:])

    # If the left neighbor is greater, search in the left subarray
    return find_peak(arr[:mid])
    # FIXME: print(find_peak([4, 2, 1, 2, 2, 2, 3, 1])) returns 2 instead of 4
