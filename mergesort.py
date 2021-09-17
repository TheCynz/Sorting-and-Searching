

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]  # all from left of middle
        right_arr = arr[len(arr)//2:]  # all to right of middle

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0  # left most eliment of left array
        j = 0  # left most eliment of right array
        k = 0  # merged array index

        while i < len(left_arr) and j < len(right_arr):
           if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
merge_sort(arr_test)

print(arr_test)
