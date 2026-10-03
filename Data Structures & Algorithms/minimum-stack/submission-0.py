class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.prefix_stack) == 0) or (val < self.prefix_stack[-1]):
            self.prefix_stack.append(val)
        else:
            self.prefix_stack.append(self.prefix_stack[-1])

    def pop(self) -> None:
        del self.stack[-1]
        del self.prefix_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_stack[-1]
        
