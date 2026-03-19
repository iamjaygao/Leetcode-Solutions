class MinStack:

    def __init__(self):
        self.stack = []
        self.mini_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini_stack:
            self.mini_stack.append(val)
        else:
            self.mini_stack.append(min(val, self.mini_stack[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.mini_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()