# Linn Erle Klofta
# CSC 2720 Lab #13
# Lab time: Friday 1-1:50pm
# Due time: 04/14/2024 @ 11:59pm

import heapq

def kBiggest(lst, k):
    # Create a min heap with the first k elements of the list
    heap = lst[:k]
    heapq.heapify(heap)
    
    # Iterate over the remaining elements of the list
    for num in lst[k:]:
        if num > heap[0]: # If the current element is larger than the smallest element in the heap,
            heapq.heapreplace(heap, num) # replace the smallest element with the current element

    return heap[0] # Return the k-largest element from the heap


# Test cases
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(kBiggest(lst, k)) # Expected output: 8

lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
k = 5
print(kBiggest(lst, k)) # Expected output: 6

lst = [1, 1, 1, 1, 1]
k = 2
print(kBiggest(lst, k)) # Expected output: 1

lst = [1, 2, 3, 4, 5]
k = 1
print(kBiggest(lst, k)) # Expected output: 5


"""  time and space complexity 

The time complexity of this approach is O(n log k), where n is the length of the input list and k 
is the number of largest elements we want to find. The initial creation of the min heap takes O(k) 
time, and the heapify operation takes O(k log k) time. Then, for each remaining element in the list, 
we perform a heapreplace operation, which takes O(log k) time. Since there are n-k remaining elements, 
the total time complexity is O((n-k) log k). Therefore, the overall time complexity is 
O(k + k log k + (n-k) log k)
which simplifies to O(n log k).

The space complexity of this approach is O(k), as we are maintaining a min heap of size k to store the 
k-largest elements. 

 """