from collections import deque
class MinStack:
    # two stacks, one for what value we added,
    # and one for keeping track of min
    # push --> 
    # pop --> pop first value in stack for both stack and minStack
    # top --> return first value in stack
    # getMin --> return first value in minStack
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
