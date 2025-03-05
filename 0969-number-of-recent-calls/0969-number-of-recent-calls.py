class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.first = 0
        self.second = 0

    def ping(self, t: int) -> int:
        
        self.queue.append(t)
        self.second += 1
        if self.queue:
            while (self.queue[self.first]) <t- 3000:
                self.queue.popleft()
        return len(self.queue)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)