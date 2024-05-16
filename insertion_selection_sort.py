# Linn Erle Klofta
# CSC 2720 Lab #4
# Lab time: Friday 1-1:50pm
# Due time: 02/04/2024 @ 11:59pm

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def SelectionSort(arr):
    for i, num in enumerate(arr):
        min_idx = i
        for j, val in enumerate(arr[i+1:], start=i+1):
            if val < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

input_array = [50, 11, 33, 21, 40, 50, 40, 40, 21]

output_array1 = SelectionSort(input_array)
output_array2 = InsertionSort(input_array)

print("SelectionSort Output:", output_array1)
print("InsertionSort Output:", output_array2)

"""
Big-O time analysis for insertion sort
The time complexity of insertion sort is O(n^2) in the worst case.
This is because for each element in the array, we compare it with all the previous elements to find its correct position.
In the worst case, when the array is in reverse order, we have to make n comparisons for each of the n elements.
Therefore, the time complexity is quadratic.

Big-O space analysis for insertion sort
The space complexity of insertion sort is O(1) because it only requires a constant amount of additional space.
The sorting is done in-place, meaning that the original array is modified without requiring any additional data structures.

Big-O time analysis for selection sort
The time complexity of selection sort is O(n^2) in the worst case.
This is because for each element in the array, we find the minimum element from the remaining unsorted elements and swap it with the current element.
In the worst case, when the array is in reverse order, we have to find the minimum element n times for each of the n elements.
Therefore, the time complexity is quadratic.

Big-O space analysis for selection sort
The space complexity of selection sort is O(1) because it only requires a constant amount of additional space.
The sorting is done in-place, meaning that the original array is modified without requiring any additional data structures.
"""

