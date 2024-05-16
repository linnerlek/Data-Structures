# Linn Erle Klofta
# CSC 2720 Homework #5
# Lab time: Friday 1-1:50pm
# Due time: 04/23/2024 @ 11:59pm

def is_binary_search_tree(tree):
    # Define a helper function for inorder traversal within the binary search tree
    def inorder_traversal(node_idx):
        # Check if the current node index is within the bounds of the tree
        if node_idx < len(tree):
            # Calculate the indices of the left and right children of the current node
            left_child_idx = 2 * node_idx + 1
            right_child_idx = 2 * node_idx + 2
            
            # Check if the left child exists and recursively traverse it
            if left_child_idx < len(tree) and tree[left_child_idx] is not None:
                # If the left subtree traversal returns False, propagate False upwards
                if not inorder_traversal(left_child_idx):
                    return False
            
            # Append the current node's value to the inorder_result list
            if not inorder_result:
                inorder_result.append(tree[node_idx])
            # If the current node's value is less than or equal to the previous node's value,
            # it violates the binary search tree property, so return False
            elif tree[node_idx] <= inorder_result[-1]:
                return False
            else:
                inorder_result.append(tree[node_idx])
            
            # Check if the right child exists and recursively traverse it
            if right_child_idx < len(tree) and tree[right_child_idx] is not None:
                # If the right subtree traversal returns False, propagate False upwards
                if not inorder_traversal(right_child_idx):
                    return False
            
            # If all conditions are met, return True
            return True
    
    # Initialize an empty list to store the inorder traversal result
    inorder_result = []
    # Start the inorder traversal from the root node (index 0)
    return inorder_traversal(0)

# Test case 1: valid binary search tree
input_tree = [10, 5, 15, 2, 7, 11, 25, 1]
print(is_binary_search_tree(input_tree))  # Output: True

# Test case 2: Not a binary search tree
input_tree_2 = [2, 4, 5]
print(is_binary_search_tree(input_tree_2))  # Output: False
