from collections import Counter


def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    freq_counter = Counter(nums).items()

    most_common_num = (None, 0)

    for item in freq_counter:
        if item[1] > most_common_num[1]:
            most_common_num = item

    return most_common_num[0]
