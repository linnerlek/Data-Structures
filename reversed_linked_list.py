# Linn Erle Klofta
# CSC 2720 Homework #3
# Lab time: Friday 1-1:50pm
# Due time: 03/21/2024 @ 11:59pm

class MyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = MyLinkedListNode(value)
            current = head
        else:
            current.next = MyLinkedListNode(value)
            current = current.next

    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    reversed_list = []
    current = prev
    while current is not None:
        reversed_list.append(current.value)
        current = current.next
    
    return reversed_list

# Test case
input_list = [5, 7, 1, 2, 3]
reversed_list = reverseLinkedList(input_list)
print(reversed_list)
