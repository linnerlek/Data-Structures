# Linn Erle Klofta
# CSC 2720 Lab #3
# Lab time: Friday 1-1:50pm
# Due time: 01/28/2024 @ 11:59pm


def counting_sort(arr):
    # Find the maximum element in the input list
    max_val = max(arr)

    # Create a count array to store the frequency of each element
    count = [0] * (max_val + 1)

    # Count the frequency of each element in the input list
    for num in arr:
        count[num] += 1

    # Generate the sorted output list
    output = []
    for i, count_i in enumerate(count):
        output.extend([i] * count_i)

    return output

# Test the counting_sort function with the given input list
input_list = [50, 11, 33, 21, 40, 50, 40, 40, 21]
output_list = counting_sort(input_list)
print(output_list)
