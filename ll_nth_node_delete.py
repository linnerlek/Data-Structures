# Linn Erle Klofta
# CSC 2720 Lab #7
# Lab time: Friday 1-1:50pm
# Due time: 02/25/2024 @ 11:59pm


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_nth_from_end(self, n):
        dummy = Node()
        dummy.next = self.head
        fast = slow = dummy

        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers in tandem
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Delete the nth node from the end
        slow.next = slow.next.next

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + ", "
            current = current.next
        return result[:-2]  # Remove the trailing comma and space


# Test cases
# Create a linked list
ll = LinkedList()
ll.append(50)
ll.append(11)
ll.append(33)
ll.append(21)
ll.append(40)
ll.append(71)

# Print the original linked list
print("Original Linked List:", ll)

# Delete the second last node
ll.delete_nth_from_end(2)

# Print the modified linked list
print("Modified Linked List:", ll)
