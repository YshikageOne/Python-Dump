# Counting sort algorithm

def countingSort(array):
    arrayLength = len(array)
    smallerNum = [0] * arrayLength
    sortedArray = [0] * arrayLength

    # Counting step
    print("Solution")
    print("Start the count")
    for current in range(arrayLength - 1):
        for compare in range(current + 1, arrayLength):
            if array[current] < array[compare]:
                smallerNum[compare] += 1
            else:
                smallerNum[current] += 1

        print(f"After comparing element at index {current} (value : {array[current]}): {smallerNum}")

    # Sorting step
    print("\nStaring the sorting")
    for index in range(arrayLength):
        sortedArray[smallerNum[index]] = array[index]
        print(f"Placing {array[index]} at position {smallerNum[index]}: {sortedArray}")

    return sortedArray

# main
inputArray = [60, 35, 81, 98, 14, 47]
print("Orignial Array:", inputArray)
outputArray = countingSort(inputArray)
print("\nSorted Array:", outputArray)


        