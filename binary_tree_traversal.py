# Linn Erle Klofta
# CSC 2720 Lab #10
# Lab time: Friday 1-1:50pm
# Due time: 03/24/2024 @ 11:59pm

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pre_order_traversal(root):
    if root is None:
        return []
    return [root.val] + pre_order_traversal(root.left) + pre_order_traversal(root.right)

def in_order_traversal(root):
    if root is None:
        return []
    return in_order_traversal(root.left) + [root.val] + in_order_traversal(root.right)

def post_order_traversal(root):
    if root is None:
        return []
    return post_order_traversal(root.left) + post_order_traversal(root.right) + [root.val]

# Test the code
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print("Pre-order Traversal:", pre_order_traversal(root))
print("In-order Traversal:", in_order_traversal(root))
print("Post-order Traversal:", post_order_traversal(root))