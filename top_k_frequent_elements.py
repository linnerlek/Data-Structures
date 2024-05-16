# Linn Erle Klofta
# CSC 2720 Homework #5
# Lab time: Friday 1-1:50pm
# Due time: 04/23/2024 @ 11:59pm

import heapq

# Using a sorting algorithm
def top_k_frequent_sort(nums, k):
    # Count the frequency of each number using a dictionary
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Sort the dictionary by frequency in descending order,
    # with ties broken by the element value
    sorted_freq = sorted(freq_map.items(), key=lambda x: (-x[1], x[0]))
    
    # Return the top k frequent elements
    result = []
    for i in range(k):
        result.append(sorted_freq[i][0])
    return sorted(result)  

# Using a priority queue
def top_k_frequent_pq(nums, k):
    # Count the frequency of each number using a dictionary
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Use a min heap to keep track of the top k frequent elements
    heap = []
    for num, freq in freq_map.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Return the top k frequent elements
    return [num for freq, num in heap]

# Test cases
input1 = [1, 2, 1, 3, 2, 2]
k1 = 2
print(top_k_frequent_sort(input1, k1))  # Output: [1, 2]
print(top_k_frequent_pq(input1, k1))  # Output: [1, 2]


input2 = [1]
k2 = 1
print(top_k_frequent_sort(input2, k2))  # Output: [1]
print(top_k_frequent_pq(input2, k2))  # Output: [1]

""" 
Sorting Algorithm:
The sorting algorithm first constructs a frequency map by iterating through the 
input list, which takes O(n) time and O(n) space, where n is the number of elements
in the input list. Sorting the frequency map by value using the built-in sorted() 
function takes O(n log n) time. Then, extracting the top k frequent elements by 
iterating through the sorted frequency map takes O(k) time. Overall, the time 
complexity of this approach is O(n log n) due to sorting. In terms of space 
complexity, it requires O(n) extra space for the frequency map and O(k) extra 
space for the result list. Therefore, the space complexity is O(n).

Priority Queue (Heap):
The priority queue approach also constructs a frequency map in O(n) time and O(n) 
space. Using a min heap to keep track of the top k frequent elements takes O(n log k) 
time, as each insertion and deletion operation on the heap takes O(log k) time, and 
we perform these operations for each element in the frequency map. The space complexity 
of the priority queue approach is O(k) for storing the heap. Thus, the overall time 
complexity is dominated by the heap operations, making it O(n log k). In terms of space 
complexity, it is O(k) due to the heap.

 """