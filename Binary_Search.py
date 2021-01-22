# This is basically defining two search functions in a sorted list. One is naive or line by line and the
# One is using binary search which is basically divide nd conquer!

# We gonna need two modules of random and time to show the timing analysis and proove that Binary search is faster
# than naive search

import random
import time


# defining naive search
def naive_search(our_list, our_target):
    # l = [1,2,3,4,5,7,9,45,8]
    for i in range(len(our_list)):
        if our_list[i] == our_target:
            return i
    return -1


# defining binary search
def binary_search(our_list, our_target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(our_list) - 1
    # print(f'My high and low is : ', high , low)
    # print(f'This is length: ', len(our_list))
    # if low == high:
    # return -1
    if low > high:
        return -1

    # Getting the average indices point
    midpoint = (low + high) // 2
    # print(f'My midpoint: ', midpoint)

    # If it's midpoint , then return it
    if our_list[midpoint] == our_target:
        return midpoint
    # If our_target is greater, then recurse the binary search with new low & high points
    elif our_target > our_list[midpoint]:
        return binary_search(our_list, our_target, midpoint + 1, high)
    # If our_target is lesser than the midpoint, then recurse again with new low and high points
    else:
        return binary_search(our_list, our_target, low, midpoint - 1)


if __name__ == '__main__':
    """our_source = [1, 2, 3, 4, 5]
    our_target = 4
    # print(naive_search(our_source, our_target))
    print(binary_search(our_source, our_target))"""

    # Showing Time Analysis
    new_length = 1000
    sorted_list = set()

    while len(sorted_list) < new_length:
        sorted_list.add(random.randint(-2 * new_length, 2 * new_length))
    sorted_list = sorted(list(sorted_list))

    # Timing Analysis for Naive Search
    start = time.time()
    for our_target in sorted_list:
        naive_search(sorted_list, our_target)
    end = time.time()
    naive_time = (end - start) / new_length
    print('\nNaive Search Results: ', naive_time, ' seconds')

    # Timing Analysis for Binary Search
    start = time.time()
    for our_target in sorted_list:
        binary_search(sorted_list, our_target)
    end = time.time()
    binary_time = (end - start) / new_length
    binary_time = binary_time.__radd__(0)
    print('Binary Search Results: ', binary_time, ' seconds\n')

    # Printing out the Difference in Time
    diff_time = (naive_time - binary_time) * 1000
    print('The Difference in Time is: ', diff_time, ' milli seconds')
