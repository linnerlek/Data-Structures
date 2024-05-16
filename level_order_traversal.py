from collections import deque

# Linn Erle Klofta
# CSC 2720 Lab #11
# Lab time: Friday 1-1:50pm
# Due time: 03/31/2024 @ 11:59pm

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order_traversal(root):
    # Check if the root is None
    if not root:
        return []

    result = []  # Initialize an empty list to store the level order traversal
    queue = deque([root])  # Create a deque and enqueue the root node

    while queue:  # Continue the loop until the queue is empty
        level_size = len(queue)  # Get the number of nodes in the current level
        current_level = []  # Initialize an empty list to store the nodes in the current level

        for _ in range(level_size):  # Iterate through the nodes in the current level
            node = queue.popleft()  # Dequeue the node from the left side of the queue
            current_level.append(node.val)  # Add the value of the node to the current level list

            # Enqueue the left and right child nodes if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.extend(current_level)  # Add the nodes in the current level to the result list

    return result  # Return the level order traversal result

# Test casee
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(level_order_traversal(root))  # Output: [4, 2, 6, 1, 3, 5, 7]