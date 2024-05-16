class MinStack:
    def __init__(self):
        self.stack = []  # Initialize an empty stack to store values
        self.min_stack = []  # Initialize an empty stack to store minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)  # Push the value onto the stack
        if not self.min_stack or val <= self.min_stack[-1]:
            # If the min_stack is empty or the value is less than or equal to the current minimum value,
            # push the value onto the min_stack
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            # If the value being popped from the stack is equal to the current minimum value,
            # pop the value from the min_stack as well
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]  # Return the top value of the stack

    def getMin(self) -> int:
        return self.min_stack[-1]  # Return the current minimum value from the min_stack
    

min_stack = MinStack()

# Test case 1: Push values into the stack
min_stack.push(5)
min_stack.push(2)
min_stack.push(7)
min_stack.push(1)

# Test case 2: Get the minimum value from the stack
min_value = min_stack.getMin()
print(min_value)  # Expected output: 1

# Test case 3: Pop values from the stack
min_stack.pop()
min_stack.pop()

# Test case 4: Get the top value from the stack
top_value = min_stack.top()
print(top_value)  # Expected output: 2

# Test case 5: Get the minimum value from the stack
min_value = min_stack.getMin()
print(min_value)  # Expected output: 2