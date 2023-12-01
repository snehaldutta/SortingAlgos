def radixsort(arr):
    def findMaxElement(arr_input):
        if not arr_input:
            return None

        max_ele = arr_input[0]

        for ele in arr_input[1:]:
            if ele > max_ele:
                max_ele = ele

        return max_ele

    max_input = findMaxElement(arr)
    pos = 1
    while max_input // pos > 0:
        countSort(arr, pos)
        pos *= 10


def countSort(arr_input, pos_indx):
    n = len(arr_input)
    freq_arr = [0] * 10
    ans_arr = [0] * n

    for i in range(n):
        freq_idx = (arr_input[i] // pos_indx) % 10
        freq_arr[freq_idx] += 1

    for i in range(1,10):
        freq_arr[i] += freq_arr[i - 1]

    i = n - 1
    while i >= 0:
        freq_idx = (arr_input[i] // pos_indx) % 10
        ans_arr[(freq_arr[freq_idx]) - 1] = arr_input[i]
        freq_arr[freq_idx] -= 1
        i -= 1

    for i in range(n):
        arr_input[i] = ans_arr[i]
