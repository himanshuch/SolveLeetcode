class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.stack.append((val, self.min))
        #print(self.stack)
        

    def pop(self) -> None:
        self.stack.pop()
        print(self.stack)
        if len(self.stack):
            v, minimum = self.stack[-1]
            self.min = minimum
        else:
            self.min = float('inf')

    def top(self) -> int:
        v, minimum = self.stack[-1]
        return v
        

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()