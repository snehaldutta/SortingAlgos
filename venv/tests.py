from typing import List
from insSort import insertSort
from quickSort import quickSort
from heapSort import heapSort
from radixSort import radixsort


def tests_funct_quicksort(sort_funct, xs: List[int]):
    sort_funct(xs, 0, len(xs) - 1)
    assert xs == sorted(xs), "Array is not sorted"


def tests_funct(sort_func, xs: List[int]):
    sort_func(xs)
    assert xs == sorted(xs), "Array is not sorted"


def run_tests(sort_func):
    xs_1 = [1, 4, 8, 90, 67, 45]
    tests_funct(sort_func, xs_1)

    xs_2 = [10, 8, 97, 65, 23, 45, 76, 55, 100]
    tests_funct(sort_func, xs_2)


def run_tests_quicksort(sort_funct):
    xs_3 = [1, 4, 8, 90, 67, 45]
    tests_funct_quicksort(sort_funct, xs_3)

    xs_4 = [10, 8, 97, 65, 23, 45, 76, 55, 100]
    tests_funct_quicksort(sort_funct, xs_4)


if __name__ == '__main__':
    run_tests(insertSort)
    run_tests(heapSort)
    run_tests_quicksort(quickSort)
    run_tests(radixsort)
