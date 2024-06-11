def largestElement(array):
    low = 0
    high = len(array) - 1

    # If the array is already sorted
    while low <= high:
        if array[low] <= array[high]:
            return array[high]

        middle = (low + high) // 2

        #If the middle element is largest element
        if array[middle] > array[middle + 1]:
            return array[middle]

        if array[middle] >= array[low]:
            low = middle + 1
        else:
            high = middle - 1

    return -1 # if array is empty


array = [35, 42, 5, 15, 27, 29]
print(largestElement(array))
