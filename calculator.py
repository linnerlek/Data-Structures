# Linn Erle Klofta
# CSC 2720 Homework #3
# Lab time: Friday 1-1:50pm
# Due time: 03/21/2024 @ 11:59pm

def evaluate_expression(tokens):
    stack = []  
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}

    for token in tokens:  
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)

    return stack.pop()

# Test case
expression = ["10", "2", "*", "15", "+"]
result = evaluate_expression(expression)
print(result)  # Output: 35

# Space complexity: O(n), where n is the number of elements in the tokens list
# Time complexity: O(n), where n is the number of elements in the tokens list