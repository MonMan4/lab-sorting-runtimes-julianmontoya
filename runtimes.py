#!/usr/bin/python3
'''
A simple program for measuring the runtime of sorting algorithms.
'''

import timeit
import random

# the following import line will only work if the sorting submodule has been correctly downloaded
from sorting.src.sorting import merge_sorted, quick_sorted

if __name__ == '__main__':

    # process command line parameters
    import argparse
    parser = argparse.ArgumentParser(
            prog = 'runtimes',
            description = 'measure the runtimes of sorting algorithms')
    parser.add_argument('--max_x', type=int, default=0)
    parser.add_argument('--input', choices=['sorted', 'random'], default='random')
    args = parser.parse_args()

    # print the markdown table header once, before the data rows
    print('| n | timsort | merge_sorted | quick_sorted |')
    print('|---:|---:|---:|---:|')
    
    # perform the runtime tests
    for x in range(0, args.max_x+1):

        if args.input == 'random':
            # generate a random list for us to sort;
            # the seed ensures that we generate the same random list on every run of the program
            random.seed(0)
            xs = [random.random() for i in range(2**x)]
        if args.input == 'sorted':
            # FIXME 2:
            # in this case, we should generate a list that is already sorted;
            # (it turns out to be common to run sorting algorithms on lists that are already sorted or almost sorted)
            # the timsort algorithm has extra optimizations for this case,
            # and whenever the input list is sorted, timsort will run in time Theta(n) instead of Theta(n log n)
            #
            # your specific task is to make xs be a list of all numbers between 0 and 2**x
            xs = list(range(2**x))

            # HINT:
            # use the range and list functions

        # calculate the runtimes
        runtimes = {}
        runtimes['timsort'] = timeit.timeit(lambda: sorted(xs), number=1)
        runtimes['merge_sorted'] = timeit.timeit(lambda: merge_sorted(xs), number=1)
        runtimes['quick_sorted'] = timeit.timeit(lambda: quick_sorted(xs), number=1)


        # display the runtimes as a markdown table row
        print(f"| 2**{x} | {runtimes['timsort']:.3e} | {runtimes['merge_sorted']:.3e} | {runtimes['quick_sorted']:.3e} |")
