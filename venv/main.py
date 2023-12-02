import copy
import random
import timeit
from insSort import insertSort
from heapSort import heapSort
from quickSort import quickSort
from radixSort import radixsort

import sys

sys.setrecursionlimit(10000)


def run(fn, xs):
    cpy = copy.deepcopy(xs)

    auto_start = timeit.default_timer()
    fn(cpy)
    auto_end = timeit.default_timer()

    assert sorted(cpy) == cpy

    return (auto_end - auto_start) * 1e9


def run_quicksort(fn, ms):
    cpy1 = copy.deepcopy(ms)

    auto_start = timeit.default_timer()
    fn(cpy1, 0, len(cpy1) - 1)
    auto_end = timeit.default_timer()

    assert sorted(cpy1) == cpy1

    return (auto_end - auto_start) * 1e9


times = 100

print("size insertion quicksort heapsort radixsort insertion_sorted quicksort_sorted heapsort_sorted radixsort_sorted")
for power in [10 ** i for i in range(4)]:
    for d in range(1, 10):
        size = d * power

        dist = (0,1000 * size)

        insert = 0
        quick = 0
        heap = 0
        radix = 0

        insert_sorted = 0
        quick_sorted = 0
        heap_sorted = 0
        radix_sorted = 0

        for t in range(times):
            haystack = [random.randint(*dist) for _ in range(size)]
            insert += run(insertSort, haystack)
            quick += run_quicksort(quickSort, haystack)
            heap += run(heapSort, haystack)
            radix += run(radixsort, haystack)

            haystack_sorted = list(range(size))

            insert_sorted += run(insertSort, haystack_sorted)
            quick_sorted += run_quicksort(quickSort, haystack_sorted)
            heap_sorted += run(heapSort, haystack_sorted)
            radix_sorted += run(radixsort, haystack_sorted)

        print(
            size,
            insert / times,
            quick / times,
            heap / times,
            radix / times,
            insert_sorted / times,
            quick_sorted / times,
            heap_sorted / times,
            radix_sorted / times
        )