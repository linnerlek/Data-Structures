# Linn Erle Klofta
# CSC 2720 Homework #3
# Lab time: Friday 1-1:50pm
# Due time: 03/21/2024 @ 11:59pm

def hasBalancedParentheses(s):
    stack = []
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            if opening.index(stack.pop()) != closing.index(char):
                return False
    
    return len(stack) == 0

# Test cases
test_cases = [
    "()",  # Balanced parentheses
    "([]{})",  # Balanced parentheses
    "([{}])()",  # Balanced parentheses
    ")",  # Unbalanced parentheses
    "([)",  # Unbalanced parentheses
    "()(()]){)}"  # Unbalanced parentheses
]

for test_case in test_cases:
    result = hasBalancedParentheses(test_case)
    print(f"{test_case}: {result}")

# Time complexity: O(n), where n is the length of the input string.
# Space complexity: O(n), where n is the length of the input string.