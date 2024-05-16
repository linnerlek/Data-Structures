# Linn Erle Klofta
# CSC 2720 Homework #4
# Lab time: Friday 1-1:50pm
# Due time: 04/09/2024 @ 11:59pm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def deleteRoot(root):
    if root is None:
        return None
    elif root.left is None and root.right is None:
        return None
    elif root.left is None:
        return root.right
    elif root.right is None:
        return root.left
    else:
        successor = findSuccessor(root.right)
        root.val = successor.val
        root.right = deleteNode(root.right, successor.val)
        return root

def findSuccessor(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return None
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            successor = findSuccessor(root.right)
            root.val = successor.val
            root.right = deleteNode(root.right, successor.val)
    return root

def inOrderTraversal(root):
    if root is None:
        return []
    return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right)

# Sample Binary Tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# Delete root node
root = deleteRoot(root)

# Perform In-Order Traversal
inOrder = inOrderTraversal(root)
print(inOrder)