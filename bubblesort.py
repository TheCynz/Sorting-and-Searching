# Python program for implementation of Bubble Sort

def bubbleSort(arr):
    #n = new_func(arr)
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def new_func(arr):
    n = len(arr)
    return n


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print(f"Sorted array is: {arr}")
"""
for i in range(len(arr)):
    print("%d" % arr[i]),"""
"""
Input: 
N = 5
arr[] = {4, 1, 3, 9, 7}
Output: 
1 3 4 7 9
"""
