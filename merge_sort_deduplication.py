# Linn Erle Klofta
# CSC 2720 Lab #5
# Lab time: Friday 1-1:50pm
# Due time: 02/11/2024 @ 11:59pm

# Using Merge Sort to deduplicate a list of video IDs
def merge_sort(arr):  # O(n log n)
    if len(arr) <= 1:  # O(1)
        return arr

    mid = len(arr) // 2  # O(1)
    left = merge_sort(arr[:mid])  # O(n log n)
    right = merge_sort(arr[mid:])  # O(n log n)

    return merge(left, right)  # O(n)


def merge(left, right):  # O(n)
    merged = []  # O(1)
    i = j = 0  # O(1)

    while i < len(left) and j < len(right):  # O(n)
        if left[i] < right[j]:  # O(1)
            merged.append(left[i])  # O(1)
            i += 1  # O(1)
        elif left[i] > right[j]:  # O(1)
            merged.append(right[j])  # O(1)
            j += 1  # O(1)
        else:  # O(1)
            i += 1  # O(1)

    merged.extend(left[i:])  # O(n)
    merged.extend(right[j:])  # O(n)

    return merged  # O(n)


def deduplicate_videos(lst):  # O(n log n)
    sorted_lst = merge_sort(lst)  # O(n log n)
    deduplicated_lst = []  # O(1)

    for i, video_id in enumerate(sorted_lst):  # O(n)
        if i == 0 or video_id != sorted_lst[i-1]:  # O(1)
            deduplicated_lst.append(video_id)  # O(1)

    return deduplicated_lst  # O(n)


# Test cases:
# Case 1: Empty list
print(deduplicate_videos([]))  # Output: []

# Case 2: List with one element
print(deduplicate_videos([50]))  # Output: [50]

# Case 3: List with duplicate elements
# Output: [11, 21, 33, 40, 50]
print(deduplicate_videos([50, 11, 33, 21, 40, 50, 40, 40, 21]))

# Case 4: List with no duplicate elements
print(deduplicate_videos([11, 21, 33, 40, 50]))  # Output: [11, 21, 33, 40, 50]
