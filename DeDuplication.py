# Linn Erle Klofta
# CSC 2720 Lab #2
# Lab time: Friday 1-1:50pm
# Due time: 01/21/2024 @ 11:59pm

# Program description: Removes duplicates from a list of integers and uses binary search to find a number in the list

def BinarySearch(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    checks = 0

    while low <= high:
        mid = (low + high) // 2
        checks += 1

        if sorted_list[mid] == target:
            return checks

        elif sorted_list[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def DeDuplication(input_list):
    max_element = max(input_list)
    counting_list = [0] * (max_element + 1)

    for num in input_list:
        counting_list[num] += 1

    output_list = []
    for i, count in enumerate(counting_list):
        if count != 0:
            output_list.append(i)

    return output_list


# Test scenarios
input_list1 = [50, 11, 33, 21, 40, 50, 40, 40, 21]
output_list1 = DeDuplication(input_list1)
print(f"List 1 output: {output_list1}.")

input_list2 = [20, 10, 30, 70, 50, 60, 40, 80, 50, 100]
output_list2 = DeDuplication(input_list2)
print(f"List 2 output: {output_list2}.")

input_list3 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
output_list3 = DeDuplication(input_list3)
print(f"List 3 output: {output_list3}.")

# Prompt user for input using a while loop to ensure valid input
while True:
    try:
        n = int(input("Enter an integer to search for in List 1: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Perform binary search on deduplicated and sorted list
result = BinarySearch(output_list1, n)

# Print result
if result != -1:
    print(f"Found {n} in {result} checks.")
else:
    print("Fail to find the input number...")
