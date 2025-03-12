class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if self.empty():
            raise IndexError("Pop from an empty stack")
        
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        top = self.q1.popleft()
        
     
        self.q1, self.q2 = self.q2, self.q1
        return top

    def top(self) -> int:
        if self.empty():
            raise IndexError("Top from an empty stack")
        
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        top = self.q1[0]
        self.q2.append(self.q1.popleft())
        
        self.q1, self.q2 = self.q2, self.q1
        return top

    def empty(self) -> bool:
        return len(self.q1) == 0
