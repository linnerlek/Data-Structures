# Linn Erle Klofta
# CSC 2720 Lab #8
# Lab time: Friday 1-1:50pm
# Due time: 03/03/2024 @ 11:59pm

class MaxQueue:
    def __init__(self):
        self.main_queue = []
        self.max_queue = []

    def enqueue(self, value):
        # Add the value to the main queue
        self.main_queue.append(value)

        # Remove elements from the back of the max queue until we find an element >= value
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()

        # Add the value to the max queue
        self.max_queue.append(value)

    def dequeue(self):
        if not self.main_queue:
            return None

        # Remove the front element from the main queue
        front = self.main_queue.pop(0)

        # If the front element is also the front of the max queue, remove it from the max queue
        if front == self.max_queue[0]:
            self.max_queue.pop(0)

        return front

    def get_max(self):
        if not self.max_queue:
            return None

        # Return the front element of the max queue
        return self.max_queue[0]


# Test cases
if __name__ == "__main__":
    # Create a MaxQueue object
    max_queue = MaxQueue()

    # Enqueue elements
    max_queue.enqueue(1)
    max_queue.enqueue(4)
    max_queue.enqueue(2)
    max_queue.enqueue(3)

    # Dequeue elements
    print(max_queue.dequeue())  # Output: 1
    print(max_queue.dequeue())  # Output: 4

    # Get the maximum value
    print(max_queue.get_max())  # Output: 3
