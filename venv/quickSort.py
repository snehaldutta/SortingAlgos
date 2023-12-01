def swap(arr, i, j):
    if i != j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


def quickSort(arr, st, end):
    if st < end:
        pi = part(arr, st, end)
        quickSort(arr, st, pi - 1)
        quickSort(arr, pi + 1, end)


def part(arr, st, end):
    pivotIdx = st
    pivot = arr[pivotIdx]

    while st < end:
        while st < len(arr) and arr[st] <= pivot:
            st += 1
        while arr[end] > pivot:
            end -= 1

        if st < end:
            swap(arr, st, end)

    swap(arr, pivotIdx, end)
    return end


