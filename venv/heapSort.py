def heapify(arr, n, i):
    max_element = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[max_element]:
        max_element = left

    if right < n and arr[right] > arr[max_element]:
        max_element = right

    if max_element != i:
        arr[i], arr[max_element] = arr[max_element], arr[i]
        heapify(arr, n, max_element)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)


