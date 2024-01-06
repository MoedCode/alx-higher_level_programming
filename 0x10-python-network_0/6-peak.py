#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Finds a peak in the list_of_integers.

    Args:
        list_of_integers (list): The list of unsorted integers.

    Returns:
        int or None: The peak element if found, None if the list is empty or None.
    """

    # Check if the list is empty or None
    if list_of_integers is None or list_of_integers == []:
        return None

    # Initialize variables for binary search
    low_index = 0
    high_index = len(list_of_integers)
    middle_index = ((high_index - low_index) // 2) + low_index
    middle_index = int(middle_index)

    # Base cases for lists of size 1 or 2
    if high_index == 1:
        return list_of_integers[0]
    if high_index == 2:
        return max(list_of_integers)

    # Check if the middle element is a peak
    if (
        list_of_integers[middle_index] >= list_of_integers[middle_index - 1]
        and list_of_integers[middle_index] >= list_of_integers[middle_index + 1]
    ):
        return list_of_integers[middle_index]

    # Recursively search in the right half if the peak is on the right
    if middle_index > 0 and list_of_integers[middle_index] < list_of_integers[middle_index + 1]:
        return find_peak(list_of_integers[middle_index:])

    # Recursively search in the left half if the peak is on the left
    if middle_index > 0 and list_of_integers[middle_index] < list_of_integers[middle_index - 1]:
        return find_peak(list_of_integers[:middle_index])
