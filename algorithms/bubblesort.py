'''The classic Bubble sort algorithm for sorting a list of numbers.

This is a simple yet optimised version which takes into account the fact
that after each pass, the elements after the last swap are already sorted
and do not need to be checked again.  This allows us to skip over a lot of 
the elements, resulting in about a worst case 50% improvement in comparison 
count (though no improvement in swap counts), and adds very little complexity

From https://en.wikipedia.org/wiki/Bubble_sort
'''

def bubble_sort(l):
    n = len(l)

    if n <= 1:
        return l
    
    while n > 0:
        newn = 0
        for i in range(1, n):
            if l[i-1] > l[i]:
                l[i-1], l[i] = l[i], l[i-1]
                newn = i
        n = newn

    return l

import random
random.seed(310118)

unsorted = [ random.randint(-100, 100) for i in range(20) ]
print 'Unsorted list:\t', unsorted
print 'Sorted list:\t', bubble_sort(unsorted)
