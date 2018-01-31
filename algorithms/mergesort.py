'''The classic merge sort algorithm.

Recursive top-down implementation using lists. From https://en.wikipedia.org/wiki/Merge_sort
'''

import random

def merge(left, right):
    '''Merges the left and right sublists
    '''

    result = []

    while len(left) and len(right):
        lfirst = left[0]
        rfirst = right[0]
        if lfirst <= rfirst:
            result.append(lfirst)
            del left[0]
        else:
            result.append(rfirst)
            del right[0]

    # either left or right may have elements left; consume them
    # only one of the following loops will actually be entered
    while len(left):
        result.append(left[0])
        del left[0]
    while len(right):
        result.append(right[0])
        del right[0]

    return result
    
def merge_sort(l):
    # Base case: a list with zero or one elements is sorted by definition.
    if len(l) <= 1:
        return l

    # Recursive case.
    # First, divide the list into equal-sized sublists
    # consisting of the first and second half of the list.
    left = []
    right = []
    for i, item in enumerate(l):
        if i < len(l) / 2:
            left.append(item)
        else:
            right.append(item)

    # Recursively sort both sublists
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the now-sorted sublists
    return merge(left, right)

unsorted = [ random.randint(-100, 100) for i in range(30) ]
print 'Unsorted list:\t', unsorted
print 'Sorted list:\t', merge_sort(unsorted)
