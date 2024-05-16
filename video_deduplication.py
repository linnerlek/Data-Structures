# Linn Erle Klofta
# CSC 2720 Lab #6
# Lab time: Friday 1-1:50pm
# Due time: 02/18/2024 @ 11:59pm


def quick_sort(arr):
    # Base case: if the array is empty or contains only one element, return the array
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (in this case, the last element)
    pivot = arr[-1]

    # Partition the array into two sub-arrays based on the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right sub-arrays
    return quick_sort(left) + middle + quick_sort(right)


def deduplicate_videos(lst):
    # Sort the list using Quick Sort algorithm
    sorted_lst = quick_sort(lst)

    # Remove duplicate elements
    deduplicated_lst = []
    for i, num in enumerate(sorted_lst):
        if i == 0 or num != sorted_lst[i-1]:
            deduplicated_lst.append(num)

    return deduplicated_lst


# Test cases
# Case 1: Normal case with duplicate elements
input_lst = [50, 11, 33, 21, 40, 50, 40, 40, 21]
expected_output = [11, 21, 33, 40, 50]
output = deduplicate_videos(input_lst)
print(output)  # Expected output: [11, 21, 33, 40, 50]

# Case 2: Empty input list
input_lst = []
expected_output = []
output = deduplicate_videos(input_lst)
print(output)  # Expected output: []

# Case 3: Input list with only one element
input_lst = [50]
expected_output = [50]
output = deduplicate_videos(input_lst)
print(output)  # Expected output: [50]

# Case 4: Input list with no duplicate elements
input_lst = [21, 11, 50, 40, 33]
expected_output = [11, 21, 33, 40, 50]
output = deduplicate_videos(input_lst)
print(output)  # Expected output: [11, 21, 33, 40, 50]

# Case 5: Input list with all elements being the same
input_lst = [40, 40, 40, 40, 40]
expected_output = [40]
output = deduplicate_videos(input_lst)
print(output)  # Expected output: [40]
