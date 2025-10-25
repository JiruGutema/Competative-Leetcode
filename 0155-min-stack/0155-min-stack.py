class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if(self.minStack):
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.mainStack:
            self.minStack.pop()
            return self.mainStack.pop()
        
    def top(self) -> int:
        if(self.mainStack):
            return self.mainStack[-1]
        return -1

    def getMin(self) -> int:
        if(self.minStack):
            return self.minStack[-1]
        return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()