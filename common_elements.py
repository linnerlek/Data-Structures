# Linn Erle Klofta
# CSC 2720 Homework #1
# Lab time: Friday 1-1:50pm
# Due time: 02/06/2024 @ 11:59pm

# Solution 1: O(mn) time complexity
def loop_join(lst1, lst2):
    common_elements = []
    for num1 in lst1:  # Iterate over each element in lst1
        for num2 in lst2:  # Iterate over each element in lst2
            if num1 == num2 and num1 not in common_elements:  # Check if num1 is equal to num2 and not already in common_elements
                common_elements.append(num1)  # Add num1 to common_elements
    return common_elements  # Return the list of common elements

# Solution 2: O(nlog(m)) or O(mlog(n)) time complexity
def loop_join_binary_search(lst1, lst2):
    common_elements = []
    for num2 in lst2:  # Iterate over each element in lst2
        if binary_search(lst1, num2) and num2 not in common_elements:  # Check if num2 is present in lst1 using binary search and not already in common_elements
            common_elements.append(num2)  # Add num2 to common_elements
    return common_elements  # Return the list of common elements

def binary_search(lst, target):
    low = 0  # Initialize the lower bound of the search range
    high = len(lst) - 1  # Initialize the upper bound of the search range
    while low <= high:  # Perform binary search until the search range is valid
        mid = (low + high) // 2  # Calculate the middle index of the search range
        if lst[mid] == target:  # Check if the middle element is equal to the target
            return True  # Return True if the target is found
        elif lst[mid] < target:  # If the middle element is less than the target
            low = mid + 1  # Update the lower bound to search in the right half of the list
        else:  # If the middle element is greater than the target
            high = mid - 1  # Update the upper bound to search in the left half of the list
    return False  # Return False if the target is not found

""" To improve Solution 2 and achieve linear time complexity, we can leverage the fact that both 
lists are already sorted. We can use a two-pointer approach, where we initialize two pointers, 
one for each list. We compare the elements at the pointers and move the pointers accordingly. 
If the elements are equal, we add it to the common_elements list and increment both pointers. 
If the element in the first list is smaller, we increment the first pointer, and if the element in 
the second list is smaller, we increment the second pointer. This approach eliminates the need 
for binary search and reduces the time complexity to O(m + n). """


# Solution 3: O(m + n) time complexity
def loop_join_linear(lst1, lst2):
    common_elements = []  # Initialize an empty list to store the common elements
    i = 0  # Initialize a pointer for lst1
    j = 0  # Initialize a pointer for lst2
    while i < len(lst1) and j < len(lst2):  # Iterate until either pointer reaches the end of its respective list
        if lst1[i] == lst2[j]:  # Check if the elements at the current pointers are equal
            common_elements.append(lst1[i])  # Add the common element to the common_elements list
            i += 1  # Move the pointer for lst1 to the next element
            j += 1  # Move the pointer for lst2 to the next element
        elif lst1[i] < lst2[j]:  # Check if the element in lst1 is smaller than the element in lst2
            i += 1  # Move the pointer for lst1 to the next element
        else:  # If the element in lst2 is smaller than the element in lst1
            j += 1  # Move the pointer for lst2 to the next element
    return common_elements  # Return the list of common elements

# Test cases
lst1 = [1, 5, 6, 6, 9, 9, 9, 11, 11, 21]
lst2 = [6, 6, 9, 11, 21, 21, 21]

# Test case 1: Null input case
lst3 = []
lst4 = []
print(loop_join(lst3, lst4))  # Output: []

# Test case 2: Length of the list is one
lst5 = [5]
lst6 = [5]
print(loop_join(lst5, lst6))  # Output: [5]

# Test case 3: Common elements exist
print(loop_join(lst1, lst2))  # Output: [6, 9, 11, 21]

# Test case 4: No common elements
lst7 = [1, 2, 3]
lst8 = [4, 5, 6]
print(loop_join(lst7, lst8))  # Output: []

# Test case 5: Common elements exist (binary search)
print(loop_join_binary_search(lst1, lst2))  # Output: [6, 9, 11, 21]