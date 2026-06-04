class MinStack:

    def __init__(self):
        self.stack = []      # Main stack
        self.min_stack = []  # Stack to store minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)

        # If min_stack is empty OR val is smaller/equal to current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # If top element is the current minimum
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
